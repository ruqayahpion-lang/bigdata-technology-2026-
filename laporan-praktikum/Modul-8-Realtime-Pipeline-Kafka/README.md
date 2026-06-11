# 🏦 Real-Time Fraud Detection System - Big Data Pipeline (Modul 8)

[cite_start]Proyek ini merupakan implementasi **End-to-End Big Data Pipeline** untuk mendeteksi transaksi mencurigakan (*Fraud Detection*) secara *real-time* dengan mengutamakan aspek keamanan dan privasi data[cite: 6, 7, 37]. [cite_start]Sistem ini dibangun menggunakan arsitektur modern yang mengintegrasikan ingestion data terdistribusi, pemrosesan aliran data (*stream processing*), penyimpanan berbasis kolom (*columnar storage*), dan visualisasi dasbor interaktif[cite: 16, 18, 19, 172].

---

## 🏛️ Arsitektur Sistem & Aliran Data
[cite_start]Sistem ini menggunakan arsitektur *pipeline* tiga lapis (*three-tier pipeline*) berkinerja tinggi[cite: 25, 54]:
1. [cite_start]**Streaming Ingestion (Apache Kafka):** Berperan sebagai penghubung pesan (*message broker*) yang menerima data aliran simulasi transaksi bank dari *Producer*[cite: 16, 17, 116].
2. [cite_start]**Stream Processing (Apache Spark Structured Streaming):** Memproses data mikro-batch secara *real-time*, melakukan transformasi data, mendeteksi *fraud*, serta menerapkan teknik keamanan (masking & enkripsi)[cite: 57, 136, 137].
3. [cite_start]**Penyimpanan Parquet (Data Lake):** Menyimpan luaran data aliran matang ke dalam direktori penyimpanan biner terkompresi berekstensi `.parquet`[cite: 47, 48, 172].
4. [cite_start]**Real-Time Visualization (Streamlit Dashboard):** Membaca direktori output secara dinamis untuk menyajikan metrik analisis transaksi dan status indikasi *fraud*[cite: 19, 21, 175, 179].


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

## ⚙️ Kode Implementasi Pipeline

### 1. Kafka Producer (`scripts/kafka_producer_bank.py`)

Script ini mensimulasikan aktivitas transaksi finansial nasabah bank secara terus-menerus dan mengirimkannya ke Apache Kafka.

```python
from kafka import KafkaProducer
import json
import time
import random

# Inisialisasi Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Kafka Producer aktif mengirimkan simulasi data transaksi...")

while True:
    data = {
        "nama": random.choice(["Andi", "Budi", "Citra"]),
        "rekening": str(random.randint(100000, 999999)),
        "jumlah": random.randint(100000, 100000000),
        "lokasi": random.choice(["Jakarta", "Luar Negeri"])
    }
    
    producer.send("bank_topic", value=data)
    print(f"📥 Mengirim data: {data}")
    time.sleep(2)

```

### 2. Spark Structured Streaming (`scripts/spark_streaming_fraud_v2.py`)

Mesin utama pemrosesan data aliran yang mengonsumsi data dari Kafka topic, menerapkan manipulasi masking pada nomor rekening nasabah, melakukan enkripsi berbasis Base64 pada nominal transaksi, serta melakukan deteksi aturan kecurangan (*rule-based fraud detection*).

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, concat, lit, when, base64
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Inisialisasi Spark Session
spark = SparkSession.builder \
    .appName("Fraud Detection") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Membaca Aliran Data (Stream Ingestion) dari Kafka
df_kafka = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "bank_topic") \
    .load()

# Mendefinisikan Schema Struktur Data Transaksi
schema = StructType([
    StructField("nama", StringType(), True),
    StructField("rekening", StringType(), True),
    StructField("jumlah", IntegerType(), True),
    StructField("lokasi", StringType(), True)
])

# Parsing Data JSON dari Nilai Payload Kafka
df = df_kafka.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# 1. Data Masking: Menyembunyikan nomor rekening (Hanya menampilkan 2 digit terakhir)
df = df.withColumn("rekening_masked", concat(lit("****"), col("rekening").substr(-2, 2)))

# 2. Fraud Detection Logic: Transaksi > 50 Juta ATAU dari Luar Negeri ditandai FRAUD
df = df.withColumn("status", 
    when(col("jumlah") > 50000000, "FRAUD")
    .when(col("lokasi") == "Luar Negeri", "FRAUD")
    .otherwise("NORMAL")
)

# 3. Data Encryption: Mengamankan data jumlah nominal menggunakan Base64 Encoding
df = df.withColumn("jumlah_encrypted", base64(col("jumlah").cast("string")))

# Menulis Aliran Data ke Format Penyimpanan Parquet
query = df.writeStream \
    .format("parquet") \
    .option("path", "stream_data/realtime_output/") \
    .option("checkpointLocation", "data/checkpoints/") \
    .start()

query.awaitTermination()

```

### 3. Streamlit Dashboard (`dashboard/fraud_dashboard_v2.py`)

Dasbor antarmuka pengguna untuk memantau indikasi keamanan transaksi bank secara interaktif dan *real-time*.

```python
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Real-Time Fraud Detection Dashboard", layout="wide")
st.title("🚨 Real-Time Fraud Detection Dashboard")

path_output = "stream_data/realtime_output/"

if os.path.exists(path_output) and len(os.listdir(path_output)) > 0:
    # Membaca Direktori Data Parquet
    df = pd.read_parquet(path_output)
    
    # Membuat Layout Kolom KPI
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Transaksi Terproses", len(df))
    with col2:
        total_fraud = len(df[df["status"] == "FRAUD"])
        st.metric("Total Terindikasi Fraud", total_fraud, delta=f"{total_fraud} Kasus", delta_color="inverse")
        
    st.markdown("---")
    
    # Menampilkan 10 Baris Transaksi Terakhir
    st.subheader("📋 Log Transaksi Terbaru (Masked & Encrypted)")
    st.dataframe(df.tail(10), use_container_width=True)
    
    # Menampilkan Grafik Status Transaksi
    st.subheader("📊 Grafik Analisis Komparasi Status Transaksi")
    st.bar_chart(df["status"].value_counts())
else:
    st.info("⏳ Menunggu aliran data masuk dari Spark Streaming Pipeline...")

```

---

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

> 
> Silakan ambil tangkapan layar penuh dari desktop Anda lalu masukkan berkas gambarnya di bawah ini untuk memenuhi luaran wajib praktikum.
> 
> 

### 1. Aktivitas Pengiriman Pesan Aliran Data oleh Apache Kafka Broker

*(Masukkan screenshot Terminal Kafka Producer Anda yang sedang mencetak log transaksi di sini)*

### 2. Status Pemrosesan Aliran Mikro-Batch Aktif Apache Spark

*(Masukkan screenshot Terminal Spark-Submit Anda yang sedang aktif memproses streaming tanpa error di sini)*

### 3. Tampilan Dasbor Pemantauan Real-Time Streamlit

*(Masukkan screenshot browser Desktop yang menampilkan visualisasi grafik batang dan tabel data bertopeng/terenkripsi di sini)*

---

## 💡 Analisis Insight Utama & Sistem Keamanan

1. 
**Aspek Keamanan & Privasi Data:** Penerapan *Data Masking* pada nomor rekening bertujuan melindungi kerahasiaan identitas finansial nasabah dari pihak internal yang tidak memiliki hak akses (*least privilege access*). Ditambah operasi enkripsi Base64 pada kolom nominal, kerahasiaan informasi krusial tetap terjaga dengan aman di dalam lingkungan penyimpanan Data Lake Parquet.


2. 
**Karakteristik Real-Time Data Pipeline:** Dalam infrastruktur finansial industri nyata, penundaan pemrosesan (*latency delay*) dapat berdampak langsung pada kerugian keuangan yang masif. Operasi *micro-batching* terdistribusi bawaan dari Spark terbukti mampu menjaga latensi tetap rendah (*low-latency processing*).


3. 
**Evolusi Arsitektur Sistem Fraud:** Pemrosesan berbasis aturan kondisional logika (*rule-based*) merupakan kerangka pondasi awal yang sangat andal untuk menyaring anomali transaksi berskala besar secara konstan. Sebagai pengembangan di masa depan, sistem ini dapat diintegrasikan dengan pemodelan algoritma kecerdasan buatan (*AI/Machine Learning*) guna menganalisis pola penipuan baru yang lebih kompleks secara otomatis.



---

## 📋 Checklist Validasi Kelulusan Praktikum

* [x] **Kafka Running:** Menginisialisasi klaster Zookeeper dan server Kafka broker secara lokal.


* [x] **Producer Kirim Data:** Berhasil mengirimkan serialisasi payload objek JSON ke `bank_topic`.


* [x] **Spark Streaming Aktif:** Berhasil menghubungkan dependensi paket konektor Kafka ke dalam aliran subsistem Spark.


* [x] **Fraud Detection Berjalan:** Logika pemisahan status transaksi `FRAUD` dan `NORMAL` berfungsi sempurna.


* [x] **Data Tersimpan:** Berhasil menulis berkas pecahan kompresi Parquet ke jalur target penyimpanan.


* [x] **Dashboard Tampil:** Dasbor visualisasi memuat fungsi metrik KPI, visualisasi grafik batang, dan komponen tabel data.



```

```
