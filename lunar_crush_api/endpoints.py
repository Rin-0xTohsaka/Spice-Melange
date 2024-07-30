import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
API_TOKEN = os.getenv('LUNAR_API_KEY')
if not API_TOKEN:
    raise ValueError("No API key found. Please set the LUNAR_API_KEY environment variable.")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Base URL for LunarCrush API
BASE_URL = "https://lunarcrush.com/api4"

# Define endpoints for dogwifhat topic
endpoints = {
    "market_time_series": "/public/coins/wif/time-series/v2",
    "market_data": "/public/coins/wif/v1",
    "top_creators": "/public/topic/dogwifhat/creators/v1",
    "top_posts": "/public/topic/dogwifhat/posts/v1",
    "topic_time_series": "/public/topic/dogwifhat/time-series/v1",
    "topic_summary": "/public/topic/dogwifhat/v1"
}

# Function to query the API
def query_api(endpoint, params=None):
    url = BASE_URL + endpoint
    response = requests.get(url, headers=HEADERS, params=params)
    try:
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Endpoint not found: {url}")
        else:
            print(f"HTTP error occurred: {e}")
        return None

# Fetch and store data in DataFrames
dataframes = {}

# Function to safely convert API response to DataFrame
def convert_to_dataframe(data, key):
    if data is None:
        return pd.DataFrame()
    if key in data and isinstance(data[key], list):
        return pd.DataFrame(data[key])
    elif key in data and isinstance(data[key], dict):
        return pd.DataFrame([data[key]])
    else:
        print(f"Unexpected data format for key '{key}': {data}")
        return pd.DataFrame()

# Market Time Series Data
params_time_series = {
    "interval": "1w",
    "bucket": "hour"
}
market_time_series = query_api(endpoints["market_time_series"], params=params_time_series)
dataframes["market_time_series"] = convert_to_dataframe(market_time_series, 'data')

# Market Data
market_data = query_api(endpoints["market_data"])
dataframes["market_data"] = convert_to_dataframe(market_data, 'data')

# Top Creators
top_creators = query_api(endpoints["top_creators"])
dataframes["top_creators"] = convert_to_dataframe(top_creators, 'data')

# Top Posts
top_posts = query_api(endpoints["top_posts"])
dataframes["top_posts"] = convert_to_dataframe(top_posts, 'data')

# Topic Time Series
topic_time_series = query_api(endpoints["topic_time_series"], params=params_time_series)
dataframes["topic_time_series"] = convert_to_dataframe(topic_time_series, 'data')

# Topic Summary
topic_summary = query_api(endpoints["topic_summary"])
dataframes["topic_summary"] = convert_to_dataframe(topic_summary, 'data')

# Print the DataFrames to verify the data
for key, df in dataframes.items():
    print(f"\n{key.replace('_', ' ').title()} DataFrame:\n", df.head())

# Save the dataframes to CSV for inspection
for key, df in dataframes.items():
    df.to_csv(f"{key}.csv", index=False)

print("Data has been saved to CSV files.")
