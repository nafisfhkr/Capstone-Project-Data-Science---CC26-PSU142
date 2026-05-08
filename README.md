fluensy-budget-optimizer/
├── app.py                     # File utama dashboard Streamlit
├── requirements.txt           # Daftar library (pandas, streamlit, plotly, dll)
├── kol_data_clean.csv         # Dataset hasil cleaning dari notebook
├── README.md                  # Dokumentasi utama proyek
├── notebooks/                 # Folder untuk menyimpan file riset
│   └── Data_Science_Capstone.ipynb
└── assets/                    # (Opsional) Untuk gambar logo atau screenshot
    └── fluensy_logo.png
2. Kode README.md (Optimasi Anggaran & ROI)
Gunakan kode di bawah ini untuk file README.md Anda. Dokumentasi ini menonjolkan nilai strategis proyek dalam membantu pengambilan keputusan berbasis data bagi UMKM.

Markdown
# 🚀 Fluensy: Smart Influencer Budget Optimization

**Fluensy** adalah platform analisis berbasis data yang dirancang khusus untuk membantu UMKM mengatasi kesulitan dalam memilih influencer yang relevan serta mengalokasikan anggaran kampanye secara optimal guna memaksimalkan *Return on Investment* (ROI).

## 📌 Latar Belakang
Banyak pelaku UMKM mengalami pemborosan biaya dalam *influencer marketing* karena pemilihan yang masih dilakukan secara manual tanpa tools pendukung keputusan. Proyek ini hadir sebagai solusi untuk mencocokkan influencer dengan budget yang tersedia secara lebih presisi.

## ✨ Fitur Utama Dashboard
- **Influencer Analytics:** Ringkasan ekosistem influencer berdasarkan kategori dan tier.
- **Budget Matching:** Analisis sebaran harga (*Base Rate*) untuk memastikan kesesuaian dengan kemampuan finansial UMKM.
- **Tier & Category Distribution:** Memetakan kategori influencer yang paling mendominasi pasar untuk jangkauan kampanye.
- **ROI Strategy:** Memberikan rekomendasi strategis dalam pemilihan tier (seperti Nano/Micro) yang lebih efisien bagi bisnis kecil.

## 🛠️ Tech Stack
- **Python**: Bahasa pemrograman utama.
- **Streamlit**: Framework untuk membangun dashboard interaktif.
- **Pandas & NumPy**: Untuk pemrosesan dan analisis data.
- **Plotly**: Untuk visualisasi data interaktif (Grafik ROI dan distribusi harga).

## 📁 Struktur Proyek
- `app.py`: Kode utama aplikasi Streamlit.
- `kol_data_clean.csv`: Dataset influencer yang telah dibersihkan dan siap pakai.
- `Data_Science_Capstone.ipynb`: Dokumentasi langkah-langkah *Exploratory Data Analysis* (EDA) dan pengolahan data.

## ⚙️ Cara Menjalankan Secara Lokal

1. **Clone repository:**
   ```bash
   git clone [https://github.com/username-anda/fluensy-budget-optimizer.git](https://github.com/username-anda/fluensy-budget-optimizer.git)
   cd fluensy-budget-optimizer
Install dependensi:

Bash
pip install -r requirements.txt
Jalankan dashboard:

Bash
streamlit run app.py
📈 Hasil Analisis
Dashboard ini membantu mengidentifikasi bahwa efisiensi budget dapat ditingkatkan dengan memfokuskan investasi pada tier influencer tertentu yang memiliki korelasi harga paling masuk akal terhadap potensi jangkauan pasar.

Dibuat oleh: [M NAFIS FAKHRUDIN & Jibran Tsaqif]

Project: Coding Camp powered by DBS Foundation 2026