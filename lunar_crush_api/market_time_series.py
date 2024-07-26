import os
import pandas as pd
import plotly.express as px
from .fetch_data import fetch_data
from .chart_style import apply_common_layout

def process_market_time_series():
    endpoint = "/public/coins/wif/time-series/v2"
    params = {"interval": "1w", "bucket": "hour"}
    data = fetch_data(endpoint, params=params)
    df = pd.DataFrame(data['data'])
    return df

def generate_market_time_series_charts(df):
    os.makedirs('charts', exist_ok=True)
    
    # Market Cap Over Time Chart
    fig = px.line(
        df, 
        x='time', 
        y='market_cap', 
        title='Market Cap Over Time',
        labels={
            'time': 'Time',
            'market_cap': 'Market Cap (USD)'
        }
    )
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'market_cap_over_time.html'))

    # Price Movement Over Time Chart
    fig = px.line(
        df, 
        x='time', 
        y=['open', 'close', 'high', 'low'], 
        title='Price Movement Over Time',
        labels={
            'time': 'Time',
            'value': 'Price (USD)'
        }
    )
    fig.update_layout(legend_title_text='Price Type')
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'price_movement_over_time.html'))

    # Volume and Market Cap Over Time Chart
    fig = px.line(
        df, 
        x='time', 
        y=['volume_24h', 'market_cap'], 
        title='Volume and Market Cap Over Time',
        labels={
            'time': 'Time',
            'value': 'USD'
        }
    )
    fig.update_layout(legend_title_text='Metric')
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'volume_market_cap_over_time.html'))
