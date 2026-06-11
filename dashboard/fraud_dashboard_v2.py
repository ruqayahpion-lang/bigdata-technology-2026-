import streamlit as st 
import pandas as pd 
import os
import glob

st.set_page_config(page_title="Real-Time Fraud Detection", layout="wide")
st.title("🚨 Real-Time Fraud Detection Dashboard") 

st.sidebar.markdown("### 👤 Developer Profile")
st.sidebar.info("Nama: Ruqayah\nRepo: bigdata-technology-2026-")

path_target = "stream_data/realtime_output/"

if os.path.exists(path_target) and len(glob.glob(os.path.join(path_target, "*.parquet"))) > 0:
    try:
        df = pd.read_parquet(path_target)
        if not df.empty and "status" in df.columns:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Transaksi", len(df))
            with col2:
                st.metric("Total Fraud", len(df[df["status"]=="FRAUD"])) 
            
            st.subheader("📋 Transaksi Terbaru")
            st.dataframe(df.tail(10), use_container_width=True) 
            
            st.subheader("📊 Grafik Status")
            st.bar_chart(df["status"].value_counts(), use_container_width=True)
        else:
            st.warning("⏳ File Parquet terdeteksi, namun Spark sedang memproses skema kolom. Menunggu aliran data...")
            st.metric("Total Transaksi", 0)
    except Exception as e:
        st.info("🔄 Sedang menyinkronkan data batch Parquet terbaru...")
else:
    st.info("📂 Menunggu aliran data masuk dari Apache Spark Streaming... Harap jalankan Kafka Producer dan Spark Job Anda.")
    st.metric("Total Transaksi", 0)
