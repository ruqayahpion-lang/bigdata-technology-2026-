# 🌆 Real-Time Large-Scale Analytics: Smart City Mobility
### Big Data Analytics Pipeline - Module 6 (Optimized Edition)

Proyek ini adalah pengembangan tingkat lanjut dari sistem transportasi cerdas yang berfokus pada **Visualisasi Data Skala Besar**. Sistem ini mengimplementasikan teknik optimasi agar dashboard tetap responsif meskipun menangani jutaan baris data dari *streaming pipeline*.


## 🚀 Fitur Utama (Module 6 Enhancements)
* **Window Aggregation**: Menghitung kepadatan lalu lintas per jendela waktu (1 menit) untuk mengidentifikasi tren kemacetan.
* **Large-Scale Optimization**: Menggunakan teknik *Downsampling* (hanya merender 1000 data terbaru) untuk menjaga performa dashboard.
* **Parquet Data Lake**: Sinkronisasi efisien antara Spark Structured Streaming dan Analytics Layer.
* **Real-Time Auto-Refresh**: Dashboard melakukan pembaruan otomatis setiap 5 detik (`REFRESH_INTERVAL = 5`).
---
## 🛠️ Tech Stack
* **Engine:** Apache Spark 4.1.1 (Structured Streaming)
* **Format:** Parquet (Columnar Storage)
* **Frontend:** Streamlit (Real-Time Dashboards)
* **Language:** Python 3.10+
* **Environment:** WSL2 / Linux Server
---
## 📂 Struktur Proyek
```text
bigdata-project/
├── analytics/
│   └── transportation_analytics.py # Logic: Windowing & Agregasi (Step 3)
├── dashboard/
│   └── dashboard_transportation.py # UI: Optimized Visualization (Step 4)
├── alerts/
│   └── transportation_alerts.py    # System: Real-Time Alerts
└── data/
    └── serving/                    # Data Lake: Parquet Files
```

---

## 📊 Decision-Oriented Dashboard (Insight Modul 6)

Sistem ini membagi informasi menjadi 3 layer keputusan utama sesuai standar Smart City:
1. **Operational Layer**: Monitoring langsung kendaraan (Live Trip Data & Alerts).
2. **Tactical Layer**: Optimasi armada melalui *Vehicle Distribution* dan *Traffic Density*.
3. **Strategic Layer**: Perencanaan jangka panjang menggunakan *Mobility Trend* dan *Anomaly Detection*.

---

## 📸 Hasil Implementasi (Screenshots)

<img width="1536" height="656" alt="Cuplikan layar 2026-04-24 113320" src="https://github.com/user-attachments/assets/5e556ecb-ac29-4de7-9abc-0e0ba9853ae1" />
<img width="1533" height="643" alt="Cuplikan layar 2026-04-24 113328" src="https://github.com/user-attachments/assets/e314c714-6d37-4fb3-9a7d-abab9c0b00f1" />
<img width="1521" height="650" alt="Cuplikan layar 2026-04-24 113335" src="https://github.com/user-attachments/assets/e5cbe03c-0a23-495d-9983-ab821a61220c" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-24 113144" src="https://github.com/user-attachments/assets/d1841bdc-7787-4efd-8f74-2d762ddf3497" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-24 113212" src="https://github.com/user-attachments/assets/9fc947a3-f093-4e54-97c7-3a0f0dcd344d" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-24 113226" src="https://github.com/user-attachments/assets/7dc67ef3-f9c6-40b3-a2d4-f94edf122835" />
<img width="1755" height="605" alt="Cuplikan layar 2026-04-24 113240" src="https://github.com/user-attachments/assets/4a71b65b-ba29-44e1-873a-b006d2783542" />
<img width="1799" height="685" alt="Cuplikan layar 2026-04-24 113250" src="https://github.com/user-attachments/assets/39254c84-7fcb-4e78-8a87-75b9383a6e8c" />
<img width="1782" height="688" alt="Cuplikan layar 2026-04-24 113257" src="https://github.com/user-attachments/assets/4a1a4f50-77d1-4756-932d-e0a2dd530c82" />

## ⚙️ Cara Menjalankan

1. Aktifkan simulator data: `python scripts/trip_generator.py`
2. Jalankan Spark Streaming: `spark-submit scripts/streaming_trip_layer.py`
3. Jalankan Dashboard: `streamlit run dashboard/dashboard_transportation.py`

---

**Author:** qeyy

**Institution:** Teknologi Informasi UIN Antasari Banjarmasin

**Year:** 2026

ingin Anda tambahkan?

```
