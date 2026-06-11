# ⚡ Real-Time Streaming Pipeline & Dashboard

### **Modul Praktikum 4: Streaming Processing + Real-Time Visualization**

Repository ini berisi implementasi sistem pengolahan data secara *real-time* menggunakan arsitektur **Big Data Streaming**. Proyek ini mensimulasikan aliran transaksi e-commerce yang diproses secara instan untuk menghasilkan dashboard analitik yang diperbarui secara otomatis.

---

## 🏗️ Arsitektur Real-Time Pipeline

Sistem ini dibangun dengan alur kerja sebagai berikut:
1. **Data Generator (Python)**: Mensimulasikan data transaksi masuk secara terus-menerus.
2. **Message Broker (Apache Kafka)**: Mengalirkan data melalui *topic* `ecommerce-transactions`.
3. **Streaming Engine (PySpark Streaming)**: Melakukan pemrosesan, transformasi, dan agregasi data saat data sedang mengalir.
4. **Real-Time Storage (Parquet/Memory)**: Menyimpan hasil olahan sementara untuk dikonsumsi dashboard
5. **Visualization Layer (Streamlit)**: Dashboard interaktif yang menampilkan KPI secara *live*.

## 🛠️ Stack Teknologi
**Language**: Python
**Streaming Engine**: PySpark Streaming.
**Message Broker**: Apache Kafka.
**Dashboard**: Streamlit.
**Environment**: Linux Server (WSL) & VS Code.

## 🚀 Langkah Eksekusi & Bukti Praktikum
<img width="898" height="1030" alt="Cuplikan layar 2026-04-03 071425" src="https://github.com/user-attachments/assets/22c15b4b-dfc4-4a07-8d30-7986ffccb341" />

<img width="1920" height="1080" alt="Cuplikan layar 2026-04-03 071531" src="https://github.com/user-attachments/assets/c4c45096-79fa-4b8e-abff-554b3ea87157" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-03 071612" src="https://github.com/user-attachments/assets/695490cf-856b-470c-98cc-91aeb69e14f4" />
<img width="1254" height="756" alt="Cuplikan layar 2026-04-03 073647" src="https://github.com/user-attachments/assets/31636b2e-178c-49ca-ba00-e97ee22ae2af" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-03 071723" src="https://github.com/user-attachments/assets/1a2789a5-9d7d-46d5-b7ec-9e474c9cdc5d" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-03 072356" src="https://github.com/user-attachments/assets/d922af0e-d46c-45c8-939d-61c3a551bdfb" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-03 072425" src="https://github.com/user-attachments/assets/c829c1cf-d210-4eef-9b22-2e52e9ac0363" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-04-03 072436" src="https://github.com/user-attachments/assets/ccf79821-b4b5-4522-85f9-52e01269b1a6" />
---
## 🧠 Insight dari Praktikum
Melalui praktikum ini, dapat dipahami bahwa:
**Batch vs Streaming**: Berbeda dengan praktikum sebelumnya (Batch), data di sini diproses dalam hitungan detik (*latency* rendah).
**Kafka**: Sangat penting untuk menangani lonjakan data (*buffering*) agar sistem tidak *crash*.
**Real-Time Analytics**: Memungkinkan bisnis merespons kejadian (seperti promo atau stok habis) secara instan.
---

**👨‍🏫 Lecturer:** Muhayat, M.IT **🏫 Institution:** Teknologi Informasi UIN Antasari **📅 Year:** 2026
