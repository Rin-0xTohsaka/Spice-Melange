import os
import pandas as pd
import plotly.express as px
from .fetch_data import fetch_data

def process_top_creators():
    endpoint = "/public/topic/dogwifhat/creators/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame(data['data'])
    return df

def generate_top_creators_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Data Table
    table_html = df.to_html(index=False)
    with open(os.path.join('charts', 'top_creators_table.html'), 'w') as f:
        f.write(table_html)

    # Bar Chart of Interactions
    fig = px.bar(df, x='creator_name', y='interactions_24h', title='Interactions in Last 24 Hours by Creator')
    fig.write_html(os.path.join('charts', 'interactions_24h.html'))

    # Follower Count Distribution
    fig = px.histogram(df, x='creator_followers', title='Follower Count Distribution')
    fig.write_html(os.path.join('charts', 'follower_count_distribution.html'))

    # Post Activity
    fig = px.bar(df, x='creator_name', y='creator_posts', title='Number of Posts in Last 24 Hours by Creator')
    fig.write_html(os.path.join('charts', 'post_activity.html'))
