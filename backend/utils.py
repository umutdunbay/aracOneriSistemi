import openai
import requests


# API'den veri çekme
def get_car_recommendations(car_type, min_price, max_price, engine):
    url = "http://127.0.0.1:8000/recommendations/"
    params = {
        "car_type": car_type,
        "min_price": str(min_price),
        "max_price": str(max_price),
        "engine": str(engine)
    }
    try:
        response = requests.get(url, params=params)  # http://127.0.0.1:8000/recommendations/?car_type=Sedan&min_price=1000000&max_price=2000000&engine=1.6
        response.raise_for_status()  # Hatalı yanıt varsa exception fırlatır
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching recommendations: {e}")
        return {"recommendation": "Öneri alınamadı."}


def generate_car_recommendation(car_type, min_price, max_price, engine):
    prompt = (
        f"""Aşağıda belirttiğim kriterlere uygun bir araç öner: 
        Araba Türü: {car_type}
        Fiyat Aralığı: {min_price} - {max_price}
        Motor: {engine}
        Bu kriterlere en uygun aracı detaylı olarak açıkla."""
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Sen bir araç öneri asistanısın. Kullanıcının belirttiği özelliklere uygun araç önerileri yapacaksın."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )

    return response['choices'][0]['message']['content']
