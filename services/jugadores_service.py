import os
import requests
from dotenv import load_dotenv

load_dotenv()

#Consumo de la api
SPORTMONKS_API_KEY = os.getenv("MYSPORTMONKS_API_KEY")
BASE_URL = os.getenv("SPORTMONKS_BASE_URL")

def obtener_jugadores():
    url = f"{BASE_URL}/players?api_token={SPORTMONKS_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
