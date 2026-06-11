# 🚀 Real-Time Smart Transportation Decision-Oriented System
### Big Data Analytics Pipeline - Module 5

Sistem ini adalah implementasi **End-to-End Big Data Pipeline** yang dirancang untuk mendukung pengambilan keputusan otomatis (Decision-Oriented System) dalam ekosistem Smart City. Sistem memproses data perjalanan transportasi secara real-time menggunakan Apache Spark dan memvisualisasikannya melalui Dashboard interaktif.

---

## 🛠️ Tech Stack
* **Engine:** Apache Spark 4.1.1 (Streaming Processing)
* **Language:** Python 3.10+
* **Frontend:** Streamlit (Real-Time Dashboard)
* **Storage:** Parquet/CSV Data Lake
* **Environment:** WSL2 (Ubuntu 22.04)

---

## 📂 Struktur Proyek
```text
bigdata-project/
├── alerts/
│   └── transportation_alerts.py    # Logika Anomali & Alert System
├── analytics/
│   └── transportation_analytics.py # Engine Analitik & Metrik
├── dashboard/
│   └── dashboard_transportation.py # UI Dashboard Streamlit
├── scripts/
│   └── trip_generator.py           # Data Source Simulator
├── stream_data/                    # Ingestion Layer (Raw JSON)
└── data/
    └── serving/                    # Serving Layer (Processed Data)


## ⚙️ Cara Menjalankan
Pastikan Virtual Environment telah aktif (`source venv/bin/activate`).
```
1. **Terminal 1: Ingestion Layer**
Menjalankan simulator data perjalanan.
```bash
python scripts/trip_generator.py
```
2. **Terminal 2: Processing Layer**
Menjalankan Spark Streaming untuk memproses data mentah.
```bash
spark-submit scripts/streaming_trip_layer.py
```
3. **Terminal 3: Visualization Layer**
Menjalankan dashboard real-time.
```bash
streamlit run dashboard/dashboard_transportation.py
```
---

## 📊 Kapabilitas Sistem (Decision Support)

Sistem ini mendukung tiga level pengambilan keputusan sesuai standar industri:
1. **Operational Decision**:
* *Live Trip Data*: Monitoring pergerakan armada secara real-time.
* *Traffic Alerts*: Notifikasi instan jika terjadi kemacetan atau lonjakan harga.
2. **Tactical Decision**:
* *Peak Hour Analysis*: Menentukan jadwal shift driver berdasarkan jam sibuk.
* *Vehicle Distribution*: Redistribusi armada ke lokasi dengan permintaan tinggi.
3. **Strategic Decision**:
* *Mobility Trend*: Analisis tren mingguan untuk rencana ekspansi wilayah.
* *Anomaly Detection*: Identifikasi transaksi mencurigakan (Fraud Detection).

---

## 📸 Dokumentasi (Screenshots)
<img width="821" height="895" alt="Cuplikan layar 2026-04-22 152736" src="https://github.com/user-attachments/assets/9ab2745a-7201-4d8f-a5c0-1a0278251adc" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-22 152758" src="https://github.com/user-attachments/assets/723fa007-690f-49c1-bbf7-e242b59fdd14" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-22 152806" src="https://github.com/user-attachments/assets/bec4ccc4-6dc0-46b5-85a0-68fb8908a7a2" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-22 152813" src="https://github.com/user-attachments/assets/45e51e59-819d-4038-83ef-481d2065b161" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-22 152300" src="https://github.com/user-attachments/assets/8be3162a-2b28-4a05-b6d0-2b335630d069" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-22 152325" src="https://github.com/user-attachments/assets/2296d35f-1b5e-44af-9fed-980df1bbc970" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-22 152337" src="https://github.com/user-attachments/assets/67f84291-5c5d-448a-aa50-d3abc761b3fd" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-22 152345" src="https://github.com/user-attachments/assets/a550e147-de27-43f6-b322-8c7f8f405814" />

**Author:** qeyy

**Project:** Praktikum Big Data Technology 2026



```
