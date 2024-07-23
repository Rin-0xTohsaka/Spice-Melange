import os
import pandas as pd
import plotly.express as px
from .fetch_data import fetch_data

def process_topic_time_series():
    endpoint = "/public/topic/dogwifhat/time-series/v1"
    params = {"interval": "1w", "bucket": "hour"}
    data = fetch_data(endpoint, params=params)
    df = pd.DataFrame(data['data'])
    return df

def generate_topic_time_series_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Data Table
    table_html = df.to_html(index=False)
    with open(os.path.join('charts', 'topic_time_series_table.html'), 'w') as f:
        f.write(table_html)

    # Interactions Over Time
    fig = px.line(df, x='time', y='interactions', title='Interactions Over Time')
    fig.write_html(os.path.join('charts', 'interactions_over_time.html'))

    # Sentiment Over Time
    fig = px.line(df, x='time', y='sentiment', title='Sentiment Over Time')
    fig.write_html(os.path.join('charts', 'sentiment_over_time.html'))

    # Post and Contributor Activity Over Time
    fig = px.line(df, x='time', y=['posts_created', 'posts_active', 'contributors_created', 'contributors_active'],
                  title='Post and Contributor Activity Over Time')
    fig.write_html(os.path.join('charts', 'post_contributor_activity.html'))

