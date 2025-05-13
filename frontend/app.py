import sys
import os
import streamlit as st

# backend modülünü doğru şekilde tanımak için path ekliyoruz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.utils import get_car_recommendations


st.set_page_config(page_title="SmartDrive", page_icon="🚗")

st.title("SmartDrive 🚗")
st.write("Yapay Zeka ile Yol Arkadaşınızı Keşfedin!")

# Araç türü seçimi
car_type = st.selectbox("Araç Türü", ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible"])

# Fiyat aralığı seçimi
min_price, max_price = st.slider("Fiyat Aralığı (TL)", 500000, 5000000, (1000000, 2000000), step=100000)

# Motor tipi filtreleme
engine_type = st.selectbox("Motor Tipini Seçin", ["Benzinli", "Dizel", "Elektrikli", "Hibrit"])

# Yıl aralığı filtreleme
year_min = st.slider("Minimum Model Yılı", min_value=1900, max_value=2025, value=2015)
year_max = st.slider("Maksimum Model Yılı", min_value=2000, max_value=2025, value=2023)

# Motor özellikleri seçimi
engine = st.selectbox("Motor Hacmi", ["1.2", "1.4", "1.6", "1.8", "2.0", "2.5"])

# Renk seçimi
car_color = st.selectbox("Aracın Rengini Seçin", ["Kırmızı", "Beyaz", "Siyah", "Mavi", "Gri", "Yeşil", "Beyaz"])

# Öneri butonu
if st.button("Öneri Al"):
    with st.spinner("Araç önerileri alınıyor..."):
        recommendations = get_car_recommendations(
            car_type, min_price, max_price, engine_type, year_min, year_max, engine
        )
        st.write("### Önerilen Araçlar:")
        if recommendations.get("recommendation"):
            st.markdown(
                f"<div style='padding: 10px; border-radius: 10px; border: 2px solid #eee;'>"
                f"{recommendations['recommendation']}</div>",
                unsafe_allow_html=True
            )
        else:
            st.write("Öneri bulunamadı.")
