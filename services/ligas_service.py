import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MYSPORTMONKS_API_KEY")
BASE_URL = os.getenv("SPORTMONKS_BASE_URL")

#Se obtiene las ligas desde la API de Sportmonks
def obtener_ligas():
    url = f"{BASE_URL}/leagues"
    params = {
        "api_token": API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()  
    else:
        return {"error": "Error al obtener las ligas", "status_code": response.status_code}
