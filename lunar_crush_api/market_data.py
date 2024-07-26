import os
import pandas as pd
import plotly.graph_objects as go
from .fetch_data import fetch_data
from .chart_style import apply_common_layout

def process_market_data():
    endpoint = "/public/coins/wif/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame([data['data']])
    return df

def generate_market_data_charts(df):
    os.makedirs('charts', exist_ok=True)

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
        go.Bar(name='24h % Change', x=[df['name'][0]], y=[df['percent_change_24h'][0]]),
        go.Bar(name='7d % Change', x=[df['name'][0]], y=[df['percent_change_7d'][0]])
    ])
    fig.update_layout(
        title='Percentage Changes',
        barmode='group',
        xaxis_title='Name',
        yaxis_title='Percent Change',
        legend_title='Change Interval'
    )
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'percentage_changes.html'))

