import streamlit as st
import time
import sys
import os

# ===============================
# FIX MODULE PATH
# ===============================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR) # Gunakan insert 0 agar prioritas

# ===============================
# IMPORTS
# ===============================
from analytics import transportation_analytics as ta
# PERBAIKAN: Gunakan alias 'alert_mod' agar tidak bentrok dengan nama variabel
from alerts import transportation_alerts as alert_mod 

# ===============================
# CONFIG
# ===============================
DATA_PATH = "data/serving/transportation"

st.set_page_config(
    page_title="Smart Transportation Dashboard", 
    layout="wide"
)

st.title("🚗 Smart Transportation Dashboard - Real-Time Analytics")

# ===============================
# AUTO REFRESH
# ===============================
REFRESH_INTERVAL = 5  # seconds
placeholder = st.empty()

# ===============================
# MAIN LOOP
# ===============================
while True:
    with placeholder.container():
        # LOAD DATA
        df = ta.load_data(DATA_PATH)

        if df.empty:
            st.warning("Waiting for streaming transportation data...")
            time.sleep(REFRESH_INTERVAL)
            continue

        # PREPROCESS
        df = ta.preprocess_data(df)

        # METRICS
        try:
            metrics = ta.calculate_metrics(df)
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Trips", metrics["total_trips"])
            col2.metric("Total Fare", f"Rp{int(metrics['total_fare']):,}")
            col3.metric("Top Location", metrics["top_location"])
        except Exception as e:
            st.error(f"Error computing metrics: {e}")

        st.divider()

        # PEAK HOURS
        try:
            # PERBAIKAN: Pastikan di transportation_analytics.py namanya 'detect_peak_hours'
            peak_val = ta.detect_peak_hours(df) 
            if peak_val is not None:
                st.info(f"🕒 Peak traffic hour: {peak_val:02d}:00")
        except Exception:
            st.warning("⚠️ Tidak dapat menghitung peak hours")

        # ALERTS (SOLUSI ERROR 'LIST OBJECT')
        try:
            # PERBAIKAN: Nama variabel 'current_alerts', nama modul 'alert_mod'
            current_alerts = alert_mod.generate_alerts(df) 
            if current_alerts:
                st.subheader("⚠️ Traffic Alerts")
                for a in current_alerts:
                    st.error(a)
        except Exception as e:
            st.warning(f"Alert error: {e}")

        # =================================
        # VISUALISASI (Langkah 4 - Optimized)
        # =================================
        try:
            v_col1, v_col2 = st.columns(2)
            with v_col1:
                st.subheader("📍 Fare per Location")
                st.bar_chart(ta.fare_per_location(df))
            with v_col2:
                st.subheader("🚗 Vehicle Distribution")
                st.bar_chart(ta.vehicle_distribution(df))

            st.subheader("📈 Mobility Trend")
            st.line_chart(ta.mobility_trend(df))

            # --- PENEMPATAN LANGKAH 4 YANG BENAR (Di luar except) ---
            st.subheader("📊 Real-Time Traffic (Windowed)") 
            traffic_window = ta.traffic_per_window(df) 
            if traffic_window is not None: 
                st.line_chart(traffic_window) 

            # Optimasi Skala Besar: Downsampling fare chart
            st.subheader("💰 Fare Trend (Sampling 1000 data)")
            df_sample = df.tail(1000) 
            if 'fare_amount' in df_sample.columns:
                st.line_chart(df_sample['fare_amount'])
            elif 'fare' in df_sample.columns:
                st.line_chart(df_sample['fare'])

        except Exception as e:
            st.warning(f"Visualization error: {e}")

        st.divider()

        # ANOMALY
        try:
            st.subheader("🚨 Anomaly Trips")
            anomaly_df = ta.detect_anomaly(df)
            if not anomaly_df.empty:
                st.dataframe(anomaly_df.tail(10), use_container_width=True)
            else:
                st.success("✅ No anomalies detected")
        except Exception as e:
            st.warning(f"Anomaly error: {e}")
        
        st.divider()

        # LIVE DATA (PERBAIKAN: Taruh di paling bawah agar tidak ganda)
        st.subheader("📋 Live Trip Data")
        st.dataframe(df.tail(20), use_container_width=True)
        
    # PERBAIKAN: time.sleep harus sejajar dengan 'with placeholder', bukan di dalam loop 'if df.empty' saja
    time.sleep(REFRESH_INTERVAL)