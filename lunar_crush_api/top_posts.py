import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .fetch_data import fetch_data
from .chart_style import apply_common_layout

def process_top_posts():
    endpoint = "/public/topic/dogwifhat/posts/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame(data['data'])
    return df

def generate_top_posts_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Create Plotly Table
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(df.columns),
            fill_color='paleturquoise',
            align='left',
            font=dict(size=12, color='black')
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            fill_color='lavender',
            align='left',
            font=dict(size=11, color='black')
        )
    )])
    fig.update_layout(title='Top Posts Table')
    fig.write_html(os.path.join('charts', 'top_posts_table.html'))

    # Interactions Over Time
    fig = px.line(
        df, 
        x='post_created', 
        y='interactions_24h', 
        title='Interactions Over Time for Top Posts',
        labels={
            'post_created': 'Post Created Time',
            'interactions_24h': 'Interactions in 24h'
        }
    )
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'interactions_over_time.html'))

    # Sentiment Distribution
    sentiment_description = "Sentiment score is between 1 and 5, where 1 is very negative, 3 is neutral, and 5 is very positive. A score of 3.5 is considered slightly positive."
    fig = px.histogram(
        df, 
        x='post_sentiment', 
        title='Sentiment Distribution for Top Posts',
        labels={
            'post_sentiment': 'Sentiment Score'
        }
    )
    fig.add_annotation(
        text=sentiment_description,
        align='left',
        showarrow=False,
        xref='paper',
        yref='paper',
        x=1,
        y=1,
        bordercolor='black',
        borderwidth=1
    )
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'sentiment_distribution.html'))

    # Top Posts by Interactions
    fig = px.bar(
        df, 
        x='post_title', 
        y='interactions_24h', 
        title='Top Posts by Interactions',
        labels={
            'post_title': 'Post Title',
            'interactions_24h': 'Interactions in 24h'
        }
    )
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'top_posts_by_interactions.html'))
