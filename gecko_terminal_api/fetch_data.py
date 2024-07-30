# gecko_terminal_api/fetch_data.py

import requests

def fetch_data(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()  # Check for HTTP errors
    return response.json()
