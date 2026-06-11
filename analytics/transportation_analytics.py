import pandas as pd
import os

# ========================
# LOAD DATA
# ========================
def load_data(path):
    if not os.path.exists(path):
        return pd.DataFrame()
    
    files = [f for f in os.listdir(path) if f.endswith('.parquet')]
    if not files:
        return pd.DataFrame()

    df = pd.concat(
        [pd.read_parquet(os.path.join(path, f)) for f in files], 
        ignore_index=True
    )
    return df

# ========================
# PREPROCESS
# ========================
def preprocess_data(df):
    if df.empty:
        return df
    
    # Perbaikan: Menghapus kurung penutup ekstra sebelum errors='coerce'
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp'])
    return df

# ========================
# METRICS
# ========================
def calculate_metrics(df):
    if df.empty:
        return {
            "total_trips": 0,
            "total_fare": 0,
            "top_location": "-"
        }
    
    # Perbaikan: Konsistensi nama kolom. Jika di preprocess pakai 'fare_amount', gunakan itu.
    # Namun modul biasanya menggunakan 'fare'. Saya sesuaikan ke 'fare' agar konsisten dengan fungsi bawah.
    fare_col = 'fare' if 'fare' in df.columns else 'fare_amount'
    
    return {
        "total_trips": len(df),
        "total_fare": df[fare_col].sum(),
        # Perbaikan logika idxmax
        "top_location": df.groupby("location")[fare_col].sum().idxmax() if not df.empty else "-"
    }

# ========================
# PEAK HOUR
# ========================
def detect_peak_hours(df):
    if df.empty or 'timestamp' not in df.columns:
        return None
    
    try:
        # Pastikan kolom timestamp benar-benar tipe datetime
        # Kita buat copy agar tidak merusak dataframe asli
        temp_df = df.copy()
        temp_df['timestamp'] = pd.to_datetime(temp_df['timestamp'])
        
        # Ambil jamnya saja
        temp_df['hour'] = temp_df['timestamp'].dt.hour
        
        # Cari jam yang paling sering muncul (modus)
        if not temp_df['hour'].empty:
            peak = temp_df['hour'].mode()
            if not peak.empty:
                return int(peak[0])
        return None
    except Exception as e:
        print(f"DEBUG PEAK HOUR ERROR: {e}")
        return None

# ========================
# VISUALIZATION DATA
# ========================

def fare_per_location(df):
    if df.empty:
        return pd.Series(dtype='float64')
    
    fare_col = 'fare' if 'fare' in df.columns else 'fare_amount'
    return df.groupby("location")[fare_col].sum().sort_values(ascending=False)

def vehicle_distribution(df):
    if df.empty:
        return pd.Series(dtype='int64')
    
    return df.groupby("vehicle_type").size().sort_values(ascending=False)

def mobility_trend(df):
    if df.empty:
        return pd.Series(dtype='float64')
    
    df = df.set_index("timestamp")
    return df["fare"].resample("10s").sum()

# =======================
# ANOMALY DETECTION
# ========================
def detect_anomaly(df):
    if df.empty:
        return pd.DataFrame()
    
    # Contoh: fare tinggi dianggap anomali sesuai threshold modul
    return df[df["fare"] > 80000]

# =======================
# AGREGASI
# =======================
def traffic_per_window(df): 
    if df.empty: 
        return None 
     
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    return (df.set_index('timestamp')
             .resample('1min')
             .size())