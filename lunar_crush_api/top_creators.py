import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .fetch_data import fetch_data
from .chart_style import apply_common_layout

def process_top_creators():
    endpoint = "/public/topic/dogwifhat/creators/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame(data['data'])
    return df

def generate_top_creators_charts(df):
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
    fig.update_layout(title='Top Creators Table')
    fig.write_html(os.path.join('charts', 'top_creators_table.html'))

    # Description for Interactions
    interactions_description = "Interactions represent the total number of publicly measurable engagements on a social post, including views, likes, comments, thumbs up, upvotes, shares, etc."

    # Bar Chart of Interactions
    fig = px.bar(
        df, 
        x='creator_name', 
        y='interactions_24h', 
        title='Interactions in Last 24 Hours by Creator',
        labels={
            'creator_name': 'Creator Name',
            'interactions_24h': 'Interactions (24h)'
        }
    )
    fig.add_annotation(
        text=interactions_description,
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
    fig.write_html(os.path.join('charts', 'interactions_24h.html'))

    # Follower Count Distribution
    fig = px.histogram(
        df, 
        x='creator_followers', 
        title='Follower Count Distribution',
        labels={
            'creator_followers': 'Number of Followers'
        }
    )
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'follower_count_distribution.html'))

    # Post Activity
    fig = px.bar(
        df, 
        x='creator_name', 
        y='creator_posts', 
        title='Number of Posts in Last 24 Hours by Creator',
        labels={
            'creator_name': 'Creator Name',
            'creator_posts': 'Posts (24h)'
        }
    )
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'post_activity.html'))
