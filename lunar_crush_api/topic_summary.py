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
        "Topic": data['data']['topic'],
        "Title": data['data']['title'],
        "Topic Rank": data['data']['topic_rank'],
        "Related Topics": ', '.join(data['data']['related_topics']),
        "Interactions (1h)": data['data']['interactions_1h'],
        "Interactions (24h)": data['data']['interactions_24h'],
        "Number of Contributors": data['data']['num_contributors'],
        "Number of Posts": data['data']['num_posts'],
        "Categories": ', '.join(data['data']['categories']),
        "Trend": data['data']['trend']
    }

    # Handle types_count, types_interactions, types_sentiment, types_sentiment_detail
    types_count = data['data']['types_count']
    for key, value in types_count.items():
        flattened_data[f"{key.replace('types_', '').replace('_', ' ').title()}"] = value

    types_interactions = data['data']['types_interactions']
    for key, value in types_interactions.items():
        flattened_data[f"{key.replace('types_', '').replace('_', ' ').title()}"] = value

    types_sentiment = data['data']['types_sentiment']
    for key, value in types_sentiment.items():
        flattened_data[f"{key.replace('types_', '').replace('_', ' ').title()}"] = value

    types_sentiment_detail = data['data']['types_sentiment_detail']
    for key, value in types_sentiment_detail.items():
        for sub_key, sub_value in value.items():
            flattened_data[f"{key.replace('types_', '').replace('_', ' ').title()} {sub_key.replace('_', ' ').title()}"] = sub_value

    df = pd.DataFrame([flattened_data])
    return df

def generate_table_html(df):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Topic Summary Table</title>
        <link rel="stylesheet" href="styles.css">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.css">
        <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.5.1.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.js"></script>
    </head>
    <body>
        <h1>Meta Summary Table</h1>
        <table id="summaryTable" class="display">
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
        <script>
            $(document).ready(function() {
                $('#summaryTable').DataTable();
            });
        </script>
    </body>
    </html>
    """

    # Prepare data for templates
    data = {
        "columns": df.columns.tolist(),
        "data": df.values.tolist()
    }

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**data)

    # Save HTML to file
    with open(os.path.join('charts', 'topic_summary_table.html'), 'w') as f:
        f.write(html_content)

def generate_wordcloud_html():
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Related Topics Word Cloud</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1>Word Cloud</h1>
        <img src="related_topics_wordcloud.png" alt="Related Topics Word Cloud">
    </body>
    </html>
    """

    # Render HTML
    template = Template(html_template)
    html_content = template.render()

    # Save HTML to file
    with open(os.path.join('charts', 'related_topics_wordcloud.html'), 'w') as f:
        f.write(html_content)

def generate_topic_summary_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Adjust column names for better readability
    df.columns = df.columns.str.replace('_', ' ').str.title()

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

    # Generate separate HTML files for the table and word cloud
    generate_table_html(df)
    generate_wordcloud_html()

if __name__ == "__main__":
    df_topic_summary = process_topic_summary()
    generate_topic_summary_charts(df_topic_summary)
