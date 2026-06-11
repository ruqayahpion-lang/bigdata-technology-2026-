
# 📊 Big Data Analytics & Visualization Dashboard

### **Modul Praktikum 3: Batch Analytics + Visualization Layer**

Repository ini berisi dokumentasi lengkap pengerjaan praktikum mata kuliah **Teknologi Big Data** yang berfokus pada alur kerja data dari *Processing Layer* hingga *Visualization Layer*.

---

## 🏗️ Arsitektur Pipeline

Dalam praktikum ini, data diolah melalui beberapa tahapan arsitektur Big Data modern:

1. **Raw Data**: Dataset mentah dalam format CSV.
2. **Processing Layer**: Menggunakan **Spark** untuk membersihkan data menjadi format **Parquet**.
3. **Analytics Layer**: Melakukan agregasi metrik bisnis (KPI) menggunakan **PySpark**.
4. **Serving Layer**: Menyimpan hasil olahan dalam format CSV agar siap dikonsumsi oleh BI Tools.
5. **Visualization Layer**: Menampilkan insight interaktif melalui **Power BI**.

## 🚀 Langkah Eksekusi & Bukti Praktikum
### 1. Analytics Layer (Back-end Processing)

Tahap ini bertujuan menghasilkan dataset yang siap untuk *Business Intelligence* (BI). Script `analytics_layer.py` menghitung total revenue, produk terlaris, dan pendapatan per kategori.

* **Perintah menjalankan script:**
```bash
source venv/bin/activate
python scripts/analytics_layer.py

```
> **📸 Screenshot**
> <img width="1032" height="1023" alt="Cuplikan layar 2026-04-02 195719" src="https://github.com/user-attachments/assets/af299572-0a49-4978-943d-1ce635675d82" />
><img width="1920" height="1080" alt="Cuplikan layar 2026-04-02 195731" src="https://github.com/user-attachments/assets/d10ab181-dd2c-410b-83c0-37545f490bda" />
> <img width="1920" height="1080" alt="Cuplikan layar 2026-04-02 195741" src="https://github.com/user-attachments/assets/b493beff-30a0-4e12-a327-98a1b521e5e2" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-02 195809" src="https://github.com/user-attachments/assets/915ca3af-56f0-42f5-8227-9337b67b3c0b" />
---

## 📈 Kesimpulan & Insight Bisnis

Melalui praktikum ini, diperoleh pemahaman kritis bahwa:
**Power BI** berperan sebagai penyaji hasil akhir, bukan mesin pemroses data besar.
* Komputasi berat dilakukan di **Spark Processing Layer**.
* Dashboard visual sangat efektif untuk membantu **Manajer** dan **Eksekutif** memahami kondisi bisnis dengan cepat.


**👨‍🏫 Lecturer:** Muhayat, M.IT **🏫 Institution:** Teknologi Informasi UIN Antasari **📅 Year:** 2026
