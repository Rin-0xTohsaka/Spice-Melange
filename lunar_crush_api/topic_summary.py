import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .fetch_data import fetch_data
from .chart_style import apply_common_layout
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def process_topic_summary():
    endpoint = "/public/topic/dogwifhat/v1"
    data = fetch_data(endpoint)
    
    # Flatten nested structures
    flattened_data = {
        "topic": data['data']['topic'],
        "title": data['data']['title'],
        "topic_rank": data['data']['topic_rank'],
        "related_topics": ', '.join(data['data']['related_topics']),
        "interactions_1h": data['data']['interactions_1h'],
        "interactions_24h": data['data']['interactions_24h'],
        "num_contributors": data['data']['num_contributors'],
        "num_posts": data['data']['num_posts'],
        "categories": ', '.join(data['data']['categories']),
        "trend": data['data']['trend']
    }

    # Handle types_count, types_interactions, types_sentiment, types_sentiment_detail
    types_count = data['data']['types_count']
    for key, value in types_count.items():
        flattened_data[f"types_count_{key}"] = value

    types_interactions = data['data']['types_interactions']
    for key, value in types_interactions.items():
        flattened_data[f"types_interactions_{key}"] = value

    types_sentiment = data['data']['types_sentiment']
    for key, value in types_sentiment.items():
        flattened_data[f"types_sentiment_{key}"] = value

    types_sentiment_detail = data['data']['types_sentiment_detail']
    for key, value in types_sentiment_detail.items():
        for sub_key, sub_value in value.items():
            flattened_data[f"types_sentiment_detail_{key}_{sub_key}"] = sub_value

    df = pd.DataFrame([flattened_data])
    return df

def generate_topic_summary_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Adjust column names for better readability
    df.columns = df.columns.str.replace('_', ' ').str.title()

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
    fig.update_layout(title='Topic Summary Table')
    fig.write_html(os.path.join('charts', 'topic_summary_table.html'))

    # Interactions by Type
    types_interactions = df[[col for col in df.columns if col.startswith("Types Interactions ")]]
    types_interactions = types_interactions.melt(var_name='Type', value_name='Interactions')
    types_interactions['Type'] = types_interactions['Type'].str.replace('Types Interactions ', '')
    fig = px.bar(
        types_interactions, 
        x='Type', 
        y='Interactions', 
        title='Interactions by Type'
    )
    fig = apply_common_layout(fig)
    fig.write_html(os.path.join('charts', 'interactions_by_type.html'))

    # Sentiment Analysis
    sentiment_description = "Sentiment score is between 1 and 100, where higher scores indicate more positive sentiment."
    types_sentiment = df[[col for col in df.columns if col.startswith("Types Sentiment ")]]
    types_sentiment = types_sentiment.melt(var_name='Type', value_name='Sentiment Score')
    types_sentiment['Type'] = types_sentiment['Type'].str.replace('Types Sentiment ', '')
    fig = px.bar(
        types_sentiment, 
        x='Type', 
        y='Sentiment Score', 
        title='Sentiment Analysis by Type'
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
    fig.write_html(os.path.join('charts', 'sentiment_analysis.html'))

    # Related Topics Word Cloud
    related_topics = df['Related Topics'].values[0]
    related_topics_str = related_topics

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(related_topics_str)
    plt.figure(figsize=(8, 4), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join('charts', 'related_topics_wordcloud.png'))
    plt.close()
