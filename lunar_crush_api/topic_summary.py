import os
import pandas as pd
import plotly.express as px
from .fetch_data import fetch_data
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def process_topic_summary():
    endpoint = "/public/topic/dogwifhat/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame([data['data']])
    return df

def generate_topic_summary_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Data Table
    table_html = df.to_html(index=False)
    with open(os.path.join('charts', 'topic_summary_table.html'), 'w') as f:
        f.write(table_html)

    # Interactions by Type
    types_interactions = pd.DataFrame(df['types_interactions'].apply(pd.Series))
    fig = px.bar(types_interactions.T, title='Interactions by Type')
    fig.update_layout(xaxis_title='Type', yaxis_title='Interactions')
    fig.write_html(os.path.join('charts', 'interactions_by_type.html'))

    # Sentiment Analysis
    types_sentiment = pd.DataFrame(df['types_sentiment'].apply(pd.Series))
    fig = px.bar(types_sentiment.T, title='Sentiment Analysis by Type')
    fig.update_layout(xaxis_title='Type', yaxis_title='Sentiment Score')
    fig.write_html(os.path.join('charts', 'sentiment_analysis.html'))

    # Related Topics Word Cloud
    related_topics = df['related_topics'].values[0]
    related_topics_str = ' '.join(related_topics)

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(related_topics_str)
    plt.figure(figsize=(8, 4), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join('charts', 'related_topics_wordcloud.png'))
    plt.close()

