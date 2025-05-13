# uvicorn backend.main:app --reload
# streamlit run frontend/app.py

import openai
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from backend.utils import generate_car_recommendation

# .env dosyasını yükle
load_dotenv()

# OpenAI API anahtarını al
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


# Araç önerisi için API endpoint
@app.get("/recommendations/")
async def get_recommendations(car_type: str, min_price: int, max_price: int, engine_type: str, year_min: int, year_max: int, engine: str):
    try:
        # Araç önerisini GPT-4o API'sinden al
        recommendation = generate_car_recommendation(car_type, min_price, max_price, engine_type, year_min, year_max, engine)
        return {"recommendation": recommendation}
    except Exception as e:
        return {"error": str(e)}