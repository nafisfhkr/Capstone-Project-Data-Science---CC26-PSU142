import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fluensy: Influencer Analytics", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Load Data
@st.cache_data
def load_data():
    # Pastikan file kol_data_clean.csv ada di folder yang sama
    df = pd.read_csv("kol_data_clean.csv")
    return df

try:
    df = load_data()
except:
    st.error("File 'kol_data_clean.csv' tidak ditemukan. Pastikan Anda sudah mengunggahnya.")
    st.stop()

st.sidebar.title("🚀 Dashboard")
st.sidebar.markdown("Smart Influencer Matching Platform")
menu = st.sidebar.selectbox("Pilih Menu:", 
    ["Ringkasan Data", "Distribusi Kategori & Tier", "Analisis Harga (Rates)", "Katalog Influencer", "Kesimpulan"])

# --- LOGIKA KONTEN ---

if menu == "Ringkasan Data":
    st.title("📊 Ringkasan Ekosistem Influencer")
    
    # Metrik Utama
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Influencer", len(df))
    m2.metric("Total Kategori", df['kategori'].nunique())
    m3.metric("Rata-rata Base Rate", f"Rp {df['base_rate'].mean():,.0f}")
    m4.metric("Tier Terbanyak", df['tier'].mode()[0])

    st.subheader("Cuplikan Data Influencer")
    st.dataframe(df.head(20), use_container_width=True)

elif menu == "Distribusi Kategori & Tier":
    st.title("🏗️ Distribusi Influencer")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Jumlah KOL per Kategori")
        fig_kat = px.bar(df['kategori'].value_counts().reset_index(), 
                         x='count', y='kategori', orientation='h',
                         color='count', color_continuous_scale='Blues')
        st.plotly_chart(fig_kat, use_container_width=True)

    with col2:
        st.subheader("Proporsi Tier Influencer")
        fig_tier = px.pie(df, names='tier', hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_tier, use_container_width=True)

    st.subheader("Peta Sebaran: Kategori vs Tier")
    pivot_data = pd.crosstab(df['kategori'], df['tier'])
    fig_heat = px.imshow(pivot_data, text_auto=True, color_continuous_scale='YlOrRd')
    st.plotly_chart(fig_heat, use_container_width=True)

elif menu == "Analisis Harga (Rates)":
    st.title("💰 Analisis Biaya & Efisiensi")
    
    st.subheader("Median Base Rate per Kategori (Juta Rp)")
    avg_rate = df.groupby('kategori')['base_rate'].median().sort_values(ascending=True) / 1e6
    fig_price = px.bar(avg_rate.reset_index(), x='base_rate', y='kategori', orientation='h')
    st.plotly_chart(fig_price, use_container_width=True)

    st.subheader("Korelasi Antar Jenis Rate")
    corr_cols = ['base_rate','story_rate','post_rate','pp_rate','addon_owning','addon_boost','addon_link']
    corr = df[corr_cols].corr()
    fig_corr = px.imshow(corr, text_auto=".2f", color_continuous_scale='RdBu_r', range_color=[-1,1])
    st.plotly_chart(fig_corr, use_container_width=True)

elif menu == "Katalog Influencer":
    st.title("🔍 Cari Influencer")
    
    # Filter
    f_kat = st.multiselect("Pilih Kategori", options=df['kategori'].unique(), default=df['kategori'].unique())
    f_tier = st.multiselect("Pilih Tier", options=df['tier'].unique(), default=df['tier'].unique())
    
    filtered_df = df[(df['kategori'].isin(f_kat)) & (df['tier'].isin(f_tier))]
    
    st.write(f"Ditemukan {len(filtered_df)} influencer sesuai kriteria.")
    st.table(filtered_df[['nama_influencer', 'kategori', 'tier', 'base_rate', 'niche']].head(50))

elif menu == "Kesimpulan":
    st.title("💡 Kesimpulan Strategis")
    st.markdown(f"""
    Berdasarkan analisis data influencer:
    1. **Dominasi Pasar:** Kategori **{df['kategori'].value_counts().idxmax()}** memiliki jumlah KOL terbanyak, cocok untuk kampanye skala besar.
    2. **Tier Terpopuler:** Influencer di tier **{df['tier'].mode()[0]}** mendominasi dataset, memberikan opsi budget yang variatif bagi UMKM.
    3. **Pricing Strategy:** Terdapat korelasi kuat antara *Base Rate* dan *Post Rate*, memudahkan estimasi budget kampanye secara keseluruhan.
    
    **Rekomendasi untuk UMKM:**
    Gunakan influencer tier **Micro** atau **Nano** di kategori yang relevan untuk mencapai ROI yang lebih efisien karena *base rate* yang lebih terjangkau namun memiliki *engagement* yang biasanya lebih niche.
    """)