import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_TOKEN = os.getenv('LUNAR_API_KEY')
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
BASE_URL = "https://lunarcrush.com/api4"

def fetch_data(endpoint, params=None):
    url = BASE_URL + endpoint
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()  # Check for HTTP errors
    return response.json()
