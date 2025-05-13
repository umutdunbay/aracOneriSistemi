import openai
import requests


# API'den veri çekme
def get_car_recommendations(car_type, min_price, max_price, engine_type, year_min, year_max, engine):
    url = "http://127.0.0.1:8000/recommendations/"
    params = {
        "car_type": car_type,
        "min_price": str(min_price),
        "max_price": str(max_price),
        "engine_type": engine_type,
        "year_min": str(year_min),
        "year_max": str(year_max),
        "engine": engine
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Hatalı yanıt varsa exception fırlatır
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching recommendations: {e}")
        return {"recommendation": "Öneri alınamadı."}


def generate_car_recommendation(car_type, min_price, max_price, engine_type, year_min, year_max, engine):
    prompt = (
        f"""Aşağıda belirttiğim kriterlere uygun birkaç araç öner:  
        Araba Türü: {car_type}
        Fiyat Aralığı: {min_price} - {max_price}
        Motor Tipi: {engine_type}
        Model Yılı: {year_min} - {year_max}
        Motor Hacmi: {engine}
        Bu kriterlere en uygun araçları sadece gerekli bilgilerle açıkla. """
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Sen bir araç öneri asistanısın. Kullanıcının belirttiği özelliklere uygun araç önerileri yapacaksın. Sanki bir satış pazarlamacısı gibi kullanıcıya samimi öneriler sunmanı istiyorum."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000
    )

    return response['choices'][0]['message']['content']
