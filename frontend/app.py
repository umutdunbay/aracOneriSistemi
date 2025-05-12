import streamlit as st
from backend.utils import get_car_recommendations

st.title("Araç Öneri Sistemi")
st.write("Yapay zeka tabanlı araç önerileri alın!")

# Kullanıcıdan giriş alın
car_type = st.selectbox("Araç Türü", ["SUV", "Sedan", "Hatchback"])
min_price = st.number_input("Minimum Fiyat", min_value=0, step=100000, value=1000000)
max_price = st.number_input("Maksimum Fiyat", min_value=0, step=100000, value=2000000)
engine = st.selectbox("Motor Hacmi", ["1.4", "1.6", "2.0", "2.5"])


# Öneri butonu
if st.button("Öneri Al"):
    recommendations = get_car_recommendations(car_type, min_price, max_price, engine)
    st.write("Öneriler:")
    st.write(recommendations.get("recommendation", "Öneri bulunamadı."))
