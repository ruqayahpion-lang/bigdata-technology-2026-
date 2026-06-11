# 🚦 Smart City Traffic AI Predictor
### Big Data Analytics Pipeline - Module 7 (Machine Learning Edition)

Repositori ini berisi implementasi **Machine Learning** menggunakan algoritma **Random Forest** untuk memprediksi kepadatan lalu lintas di lingkungan Smart City. Sistem ini mengintegrasikan data pipeline dari pembersihan data hingga deployment dashboard interaktif.

---

## 🧠 Alur Kerja Sistem (Pipeline)
1. **Data Pre-processing**: Mengubah data mentah menjadi fitur time-series (ekstraksi jam, hari, dan cuaca).
2. **Feature Engineering**: Menggunakan teknik *Shifting* untuk menciptakan variabel `lag1` (data trafik jam sebelumnya).
3. **Model Training**: Melatih regressor Random Forest dan melakukan persistensi model menggunakan `joblib`.
4. **Interactive Dashboard**: Antarmuka berbasis Streamlit untuk input parameter dan prediksi real-time.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **ML Library:** Scikit-Learn
* **Data Handling:** Pandas & NumPy
* **Visualization:** Matplotlib & Streamlit
* **Environment:** VS Code (Remote WSL)

---

## 📂 Struktur Folder
```text
bigdata-project/
├── analytics/
│   ├── traffic_ml_model_v1.py   # Script Training Model
│   └── data_cleaning.py         # Script Pre-processing
├── dashboard/
│   └── traffic_dashboard_v1.py  # AI Dashboard (Streamlit)
├── data/
│   ├── raw/                     # Dataset mentah
│   └── clean/                   # Dataset siap latih
├── models/
│   └── traffic_model_v1.pkl     # Exported AI Model

---
## 📂 Screenshots
<img width="616" height="959" alt="Cuplikan layar 2026-05-12 145409" src="https://github.com/user-attachments/assets/f34ed26a-6456-44c3-acc4-d9476603dc7b" />
<img width="1228" height="345" alt="Cuplikan layar 2026-05-12 145648" src="https://github.com/user-attachments/assets/3106ab61-4f2f-4b29-84e1-fee20441ec17" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-05-12 145300" src="https://github.com/user-attachments/assets/95b8676d-1813-4b81-a22c-1c24f2dc3161" />
<img width="1920" height="1080" alt="Cuplikan layar 2026-05-12 145311" src="https://github.com/user-attachments/assets/0a5480a3-4829-490e-96e5-7bc1a0de3d4f" />


