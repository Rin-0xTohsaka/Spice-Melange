import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data
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

    # Debugging: Print column names to verify
    print(df.columns.tolist())

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

    # HTML Template for Chart.js
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Topic Summary</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <h1>Topic Summary Table</h1>
        <table border="1">
            <thead>
                <tr>
                    {% for column in columns %}
                    <th>{{ column }}</th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in data %}
                <tr>
                    {% for cell in row %}
                    <td>{{ cell }}</td>
                    {% endfor %}
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <h1>Interactions by Type</h1>
        <canvas id="interactionsByTypeChart"></canvas>
        <script>
            var ctx = document.getElementById('interactionsByTypeChart').getContext('2d');
            var interactionsByTypeChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: {{ interaction_types | safe }},
                    datasets: [{
                        label: 'Interactions',
                        data: {{ interactions | safe }},
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        x: { title: { display: true, text: 'Type' }},
                        y: { title: { display: true, text: 'Interactions' }}
                    }
                }
            });
        </script>

        <h1>Sentiment Analysis by Type</h1>
        <canvas id="sentimentAnalysisChart"></canvas>
        <script>
            var ctx2 = document.getElementById('sentimentAnalysisChart').getContext('2d');
            var sentimentAnalysisChart = new Chart(ctx2, {
                type: 'bar',
                data: {
                    labels: {{ sentiment_types | safe }},
                    datasets: [{
                        label: 'Sentiment Score',
                        data: {{ sentiment_scores | safe }},
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        x: { title: { display: true, text: 'Type' }},
                        y: { title: { display: true, text: 'Sentiment Score' }}
                    }
                }
            });
        </script>

        <h1>Related Topics Word Cloud</h1>
        <img src="related_topics_wordcloud.png" alt="Related Topics Word Cloud">

    </body>
    </html>
    """

    # Prepare data for templates
    data = {
        "columns": df.columns.tolist(),
        "data": df.values.tolist(),
        "interaction_types": [col.replace('Types Interactions ', '') for col in df.columns if col.startswith("Types Interactions ")],
        "interactions": [df[col].iloc[0] for col in df.columns if col.startswith("Types Interactions ")],
        "sentiment_types": [col.replace('Types Sentiment ', '') for col in df.columns if col.startswith("Types Sentiment ")],
        "sentiment_scores": [df[col].iloc[0] for col in df.columns if col.startswith("Types Sentiment ")]
    }

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**data)

    # Save HTML to file
    with open(os.path.join('charts', 'topic_summary.html'), 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    df_topic_summary = process_topic_summary()
    generate_topic_summary_charts(df_topic_summary)
