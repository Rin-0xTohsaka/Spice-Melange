import requests
import pandas as pd
from dotenv import load_dotenv
import os
import plotly.express as px
import plotly.graph_objects as go

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

def process_data(data, key):
    if key in data and isinstance(data[key], list):
        return pd.DataFrame(data[key])
    elif key in data and isinstance(data[key], dict):
        return pd.DataFrame([data[key]])
    return pd.DataFrame()

def save_to_csv(df, filename):
    os.makedirs('data', exist_ok=True)
    filepath = os.path.join('data', filename)
    df.to_csv(filepath, index=False)

def generate_charts(dataframes):
    os.makedirs('charts', exist_ok=True)

    # Market Data Charts
    if "market_data" in dataframes:
        df = dataframes["market_data"]

        # Market Cap Indicator
        fig = go.Figure(go.Indicator(
            mode = "number",
            value = df['market_cap'][0],
            title = {"text": "Market Cap"},
            domain = {'x': [0, 1], 'y': [0, 1]}
        ))
        fig.write_html(os.path.join('charts', 'market_cap.html'))

        # Price Indicator with 24h change
        fig = go.Figure(go.Indicator(
            mode = "number+delta",
            value = df['price'][0],
            delta = {'reference': df['price'][0] / (1 + df['percent_change_24h'][0] / 100)},
            title = {"text": "Price (USD) - 24h Change"},
            domain = {'x': [0, 1], 'y': [0, 1]}
        ))
        fig.write_html(os.path.join('charts', 'price.html'))

        # Volume Indicator with 24h change
        fig = go.Figure(go.Indicator(
            mode = "number+delta",
            value = df['volume_24h'][0],
            delta = {'reference': df['volume_24h'][0] / (1 + df['percent_change_24h'][0] / 100)},
            title = {"text": "24h Volume (USD) - 24h Change"},
            domain = {'x': [0, 1], 'y': [0, 1]}
        ))
        fig.write_html(os.path.join('charts', 'volume_24h.html'))

        # Percentage Changes Chart
        fig = go.Figure(data=[
            go.Bar(name='24h % Change', x=df['name'], y=df['percent_change_24h']),
            go.Bar(name='7d % Change', x=df['name'], y=df['percent_change_7d'])
        ])
        fig.update_layout(title='Percentage Changes', barmode='group', xaxis_title='Name', yaxis_title='Percent Change')
        fig.write_html(os.path.join('charts', 'percentage_changes.html'))

    # Market Time Series Charts
    if "market_time_series" in dataframes:
        df = dataframes["market_time_series"]
        fig = px.line(df, x='time', y='market_cap', title='Market Cap Over Time')
        fig.write_html(os.path.join('charts', 'market_cap_over_time.html'))

    # Interactions Over Time Chart
    if "topic_time_series" in dataframes:
        df = dataframes["topic_time_series"]
        fig = px.line(df, x='time', y='interactions', title='Interactions Over Time')
        fig.write_html(os.path.join('charts', 'interactions_over_time.html'))

    # Sentiment Over Time Chart
    if "topic_time_series" in dataframes:
        df = dataframes["topic_time_series"]
        fig = px.line(df, x='time', y='sentiment', title='Sentiment Over Time')
        fig.write_html(os.path.join('charts', 'sentiment_over_time.html'))

def main():
    endpoints = {
        "market_time_series": "/public/coins/wif/time-series/v2",
        "market_data": "/public/coins/wif/v1",
        "top_creators": "/public/topic/dogwifhat/creators/v1",
        "top_posts": "/public/topic/dogwifhat/posts/v1",
        "topic_time_series": "/public/topic/dogwifhat/time-series/v1",
        "topic_summary": "/public/topic/dogwifhat/v1"
    }

    params_time_series = {"interval": "1w", "bucket": "hour"}

    dataframes = {}
    dataframes["market_time_series"] = process_data(fetch_data(endpoints["market_time_series"], params=params_time_series), 'data')
    dataframes["market_data"] = process_data(fetch_data(endpoints["market_data"]), 'data')
    dataframes["top_creators"] = process_data(fetch_data(endpoints["top_creators"]), 'data')
    dataframes["top_posts"] = process_data(fetch_data(endpoints["top_posts"]), 'data')
    dataframes["topic_time_series"] = process_data(fetch_data(endpoints["topic_time_series"], params=params_time_series), 'data')
    dataframes["topic_summary"] = process_data(fetch_data(endpoints["topic_summary"]), 'data')

    for key, df in dataframes.items():
        save_to_csv(df, f"{key}.csv")

    generate_charts(dataframes)

if __name__ == "__main__":
    main()
