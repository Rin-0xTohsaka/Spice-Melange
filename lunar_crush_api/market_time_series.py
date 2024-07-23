import os
import pandas as pd
import plotly.express as px
from .fetch_data import fetch_data

def process_market_time_series():
    endpoint = "/public/coins/wif/time-series/v2"
    params = {"interval": "1w", "bucket": "hour"}
    data = fetch_data(endpoint, params=params)
    df = pd.DataFrame(data['data'])
    return df

def generate_market_time_series_charts(df):
    os.makedirs('charts', exist_ok=True)
    fig = px.line(df, x='time', y='market_cap', title='Market Cap Over Time')
    fig.write_html(os.path.join('charts', 'market_cap_over_time.html'))
