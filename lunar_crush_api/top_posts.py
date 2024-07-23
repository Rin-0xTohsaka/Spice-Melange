import os
import pandas as pd
import plotly.express as px
from .fetch_data import fetch_data

def process_top_posts():
    endpoint = "/public/topic/dogwifhat/posts/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame(data['data'])
    return df

def generate_top_posts_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Data Table
    table_html = df.to_html(index=False)
    with open(os.path.join('charts', 'top_posts_table.html'), 'w') as f:
        f.write(table_html)

    # Interactions Over Time
    fig = px.line(df, x='post_created', y='interactions_24h', title='Interactions Over Time for Top Posts')
    fig.write_html(os.path.join('charts', 'interactions_over_time.html'))

    # Sentiment Distribution
    fig = px.histogram(df, x='post_sentiment', title='Sentiment Distribution for Top Posts')
    fig.write_html(os.path.join('charts', 'sentiment_distribution.html'))

    # Top Posts by Interactions
    fig = px.bar(df, x='post_title', y='interactions_24h', title='Top Posts by Interactions')
    fig.write_html(os.path.join('charts', 'top_posts_by_interactions.html'))

