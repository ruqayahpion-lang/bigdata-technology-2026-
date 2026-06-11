import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Traffic AI", layout="wide")  

st.title("🚦Smart Traffic AI Dashboard")

# Load data
df = pd.read_csv('data/clean/traffic_smartcity_v1.csv')

# Load model
model = joblib.load('models/traffic_model_v1.pkl')

# Feature
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.dayofweek

# PERBAIKAN: Tambahkan tanda kutip pada 'lag1'
df['lag1'] = df['traffic'].shift(1)
df = df.dropna()

# Metrics
col1, col2 = st.columns(2)

col1.metric("Avg Traffic", int(df['traffic'].mean()))
col2.metric("Max Traffic", int(df['traffic'].max()))

# chart
st.subheader("📈Traffic Trends")

c1, c2 = st.columns([0.3, 0.1])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df['traffic'].values)
st.pyplot(fig)

# Prediction
st.subheader("🔮Traffic Prediction")

hour = st.slider("Jam", 0, 23, 17)
day = st.slider("Hari", 0, 6, 2)
lag1_val = st.number_input("Traffic sebelumnya", 50, 300, 120) # Ganti nama var agar tidak bentrok

if st.button("Prediksi"):
    # Pastikan input dikirim dalam bentuk list of list/DataFrame
    pred = model.predict([[hour, day, lag1_val]])
    st.success(f"Prediksi: {int(pred[0])} kendaraan")