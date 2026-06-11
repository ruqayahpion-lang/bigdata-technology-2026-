# 🏦 Real-Time Fraud Detection System - Big Data Pipeline (Modul 8)

[cite_start]Proyek ini merupakan implementasi **End-to-End Big Data Pipeline** untuk mendeteksi transaksi mencurigakan (*Fraud Detection*) secara *real-time* dengan mengutamakan aspek keamanan dan privasi data[cite: 6, 7, 37]. [cite_start]Sistem ini dibangun menggunakan arsitektur modern yang mengintegrasikan ingestion data terdistribusi, pemrosesan aliran data (*stream processing*), penyimpanan berbasis kolom (*columnar storage*), dan visualisasi dasbor interaktif[cite: 16, 18, 19, 172].

---

## 🏛️ Arsitektur Sistem & Aliran Data
Sistem ini menggunakan arsitektur *pipeline* tiga lapis (*three-tier pipeline*) berkinerja tinggi[cite: 25, 54]:
1. **Streaming Ingestion (Apache Kafka):** Berperan sebagai penghubung pesan (*message broker*) yang menerima data aliran simulasi transaksi bank dari *Producer*
2. **Stream Processing (Apache Spark Structured Streaming):** Memproses data mikro-batch secara *real-time*, melakukan transformasi data, mendeteksi *fraud*, serta menerapkan teknik keamanan (masking & enkripsi)
3. **Penyimpanan Parquet (Data Lake):** Menyimpan luaran data aliran matang ke dalam direktori penyimpanan biner terkompresi berekstensi `.parquet`
4. Real-Time Visualization (Streamlit Dashboard):** Membaca direktori output secara dinamis untuk menyajikan metrik analisis transaksi dan status indikasi *fraud*
```

[Kafka Producer] ➡️ [Kafka Topic] ➡️ [Spark Structured Streaming] ➡️ [Parquet Storage] ➡️ [Streamlit Dashboard]

```
---

## 🛠️ Komponen Teknologi & Lingkungan Pengembangan
* [cite_start]**Bahasa Pemrograman:** Python 3 [cite: 8, 9]
* [cite_start]**Lingkungan Sistem:** Linux Server Environment / WSL (Windows Subsystem for Linux) [cite: 10, 11]
* [cite_start]**Editor Kode:** VS Code (Remote WSL) [cite: 12, 13]
* [cite_start]**Message Broker:** Apache Kafka v3.5.1 [cite: 100]
* [cite_start]**Data Processing Engine:** Apache Spark v3.5.1 (PySpark Structured Streaming) [cite: 18, 90]
* [cite_start]**Format Penyimpanan:** Apache Parquet Format [cite: 172]
* [cite_start]**Dashboard Visualisasi:** Streamlit [cite: 19, 21]

---

## 📂 Struktur Direktori Proyek (Wajib)
[cite_start]Sesuai dengan ketentuan standar laboratorium, proyek disusun mengikuti struktur folder berikut[cite: 60]:

```text
.
├── dashboard/
│   └── fraud_dashboard_v2.py      # Script Aplikasi Dasbor Streamlit
├── logs/
│   └── fraud_realtime.log         # Berkas Audit Rekaman Log Sistem
├── scripts/
│   ├── kafka_producer_bank.py     # Script Simulator Transaksi (Producer)
│   └── spark_streaming_fraud_v2.py # Script Pemrosesan Utama Spark Streaming
├── stream_data/
│   └── realtime_output/           # Direktori Target Penyimpanan File Parquet
└── README.md                      # Dokumentasi Proyek

```
---

#

## 🏃‍♂️ Panduan Menjalankan Sistem

Jalankan komponen-komponen pipeline secara berurutan menggunakan terminal terpisah:

1. **Terminal 1: Menjalankan Kafka Producer**
```bash
python scripts/kafka_producer_bank.py
```
2. **Terminal 2: Menjalankan Spark Streaming Engine**
```bash
spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  scripts/spark_streaming_fraud_v2.py
```
3. **Terminal 3: Menjalankan Dasbor Monitoring Streamlit**
```bash
streamlit run dashboard/fraud_dashboard_v2.py
```
---

## 📸 Bukti Dokumentasi Output Eksekusi (Screenshots Wajib)
<img width="1718" height="561" alt="Cuplikan layar 2026-05-28 003325" src="https://github.com/user-attachments/assets/36ed8ab0-6b92-45a5-9877-26c15b272c02" />
<img width="1569" height="583" alt="Cuplikan layar 2026-05-28 003334" src="https://github.com/user-attachments/assets/6cb6b394-70d8-4ead-8233-adc3fc98068a" />
<img width="1685" height="287" alt="Cuplikan layar 2026-05-28 003346" src="https://github.com/user-attachments/assets/2143835a-4fc2-4cf3-a558-eb7c872233d7" />
<img width="1583" height="595" alt="Cuplikan layar 2026-05-28 003403" src="https://github.com/user-attachments/assets/63c92e26-0813-4974-9966-383f4befc473" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-05-28 003124" src="https://github.com/user-attachments/assets/9e7b09ba-ec5f-49cb-8414-4a8862aa15fe" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-05-28 003134" src="https://github.com/user-attachments/assets/3ccb3576-e62b-4186-935b-419021a28643" />

## 💡 Analisis Insight Utama & Sistem Keamanan
1. **Aspek Keamanan & Privasi Data:** Penerapan *Data Masking* pada nomor rekening bertujuan melindungi kerahasiaan identitas finansial nasabah dari pihak internal yang tidak memiliki hak akses (*least privilege access*). Ditambah operasi enkripsi Base64 pada kolom nominal, kerahasiaan informasi krusial tetap terjaga dengan aman di dalam lingkungan penyimpanan Data Lake Parquet
2. **Karakteristik Real-Time Data Pipeline:** Dalam infrastruktur finansial industri nyata, penundaan pemrosesan (*latency delay*) dapat berdampak langsung pada kerugian keuangan yang masif. Operasi *micro-batching* terdistribusi bawaan dari Spark terbukti mampu menjaga latensi tetap rendah (*low-latency processing*).
3. **Evolusi Arsitektur Sistem Fraud:** Pemrosesan berbasis aturan kondisional logika (*rule-based*) merupakan kerangka pondasi awal yang sangat andal untuk menyaring anomali transaksi berskala besar secara konstan. Sebagai pengembangan di masa depan, sistem ini dapat diintegrasikan dengan pemodelan algoritma kecerdasan buatan (*AI/Machine Learning*) guna menganalisis pola penipuan baru yang lebih kompleks secara otomatis.
--

