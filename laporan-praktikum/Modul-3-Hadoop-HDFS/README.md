
# 📊 Big Data Analytics & Visualization Dashboard

### **Modul Praktikum 3: Batch Analytics + Visualization Layer**

Repository ini berisi dokumentasi lengkap pengerjaan praktikum mata kuliah **Teknologi Big Data** yang berfokus pada alur kerja data dari *Processing Layer* hingga *Visualization Layer*.

---

## 🏗️ Arsitektur Pipeline

Dalam praktikum ini, data diolah melalui beberapa tahapan arsitektur Big Data modern:

1. 
**Raw Data**: Dataset mentah dalam format CSV.


2. 
**Processing Layer**: Menggunakan **Spark** untuk membersihkan data menjadi format **Parquet**.


3. 
**Analytics Layer**: Melakukan agregasi metrik bisnis (KPI) menggunakan **PySpark**.


4. 
**Serving Layer**: Menyimpan hasil olahan dalam format CSV agar siap dikonsumsi oleh BI Tools.


5. 
**Visualization Layer**: Menampilkan insight interaktif melalui **Power BI**.



---

## 🚀 Langkah Eksekusi & Bukti Praktikum

### 1. Analytics Layer (Back-end Processing)

Tahap ini bertujuan menghasilkan dataset yang siap untuk *Business Intelligence* (BI). Script `analytics_layer.py` menghitung total revenue, produk terlaris, dan pendapatan per kategori.

* **Perintah menjalankan script:**
```bash
source venv/bin/activate
python scripts/analytics_layer.py

```



> **📸 Screenshot 1: Eksekusi Terminal**
> 
> 
> Menampilkan log "ANALYTICS LAYER COMPLETED SUCCESS" dan durasi eksekusi.
> 
> 

---

### 2. Serving Layer (Data Storage)

Setelah script dijalankan, folder `data/serving/` akan terbentuk sebagai wadah dataset KPI.

> **📸 Screenshot 2: Struktur Folder Serving**
> 
> 
> Menampilkan folder total_revenue, top_products, category_revenue, dan avg_transaction.
> 
> 

---

### 3. Visualization Layer (Dashboard Business Intelligence)

Hasil analisis dihubungkan ke Power BI untuk membuat dashboard keputusan bisnis.

| Metrik Visual | Deskripsi |
| --- | --- |
| **KPI Card** | Menampilkan Total Revenue sebesar **Rp284,070,070**.

 |
| **Top 10 Products** | Bar chart produk dengan kuantitas penjualan tertinggi.

 |
| **Revenue Category** | Perbandingan pendapatan antar kategori produk.

 |

> **📸 Screenshot 3: Dashboard Power BI Utama**
> 
> 
> Tampilan "E-Commerce Sales Dashboard" yang telah disusun rapi.
> 
> 

---

## 📈 Kesimpulan & Insight Bisnis

Melalui praktikum ini, diperoleh pemahaman kritis bahwa:

* 
**Power BI** berperan sebagai penyaji hasil akhir, bukan mesin pemroses data besar.


* Komputasi berat dilakukan di **Spark Processing Layer**.


* Dashboard visual sangat efektif untuk membantu **Manajer** dan **Eksekutif** memahami kondisi bisnis dengan cepat.



---

## 📋 Checklist Validasi

Berdasarkan rubrik penilaian modul:

* [ ] Analytics layer berhasil dijalankan.
* [ ] Folder `data/serving` terbentuk.
* [ ] Dataset berhasil diimport ke Power BI.
* [ ] KPI Total Revenue tampil dengan benar.
* [ ] Visualisasi Top Product & Category Revenue muncul.
* [ ] Dashboard memiliki judul yang sesuai.

---

**👨‍🏫 Lecturer:** Muhayat, M.IT **🏫 Institution:** Teknologi Informasi UIN Antasari **📅 Year:** 2026
