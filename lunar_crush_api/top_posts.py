import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_top_posts():
    endpoint = "/public/topic/dogwifhat/posts/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame(data['data'])
    return df

def generate_top_posts_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Ensure the data is correctly formatted
    df['post_created'] = pd.to_datetime(df['post_created'], unit='s').astype(str)
    df['post_sentiment'] = df['post_sentiment'].fillna(0)
    df['interactions_24h'] = df['interactions_24h'].fillna(0)

    # Data for Chart.js
    sentiment_distribution = {
        'labels': df['post_sentiment'].tolist()
    }

    top_posts_by_interactions = {
        'labels': df['post_title'].tolist(),
        'data': df['interactions_24h'].tolist()
    }

    # HTML Template for Chart.js and DataTables
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Top Posts Visualization</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>
        <link rel="stylesheet" href="https://cdn.datatables.net/1.10.25/css/jquery.dataTables.min.css">
    </head>
    <body>
        <h1>Top Posts Visualization</h1>

        <h2>Top Posts Table</h2>
        <table id="topPostsTable" class="display">
            <thead>
                <tr>
                    {% for col in columns %}
                    <th>{{ col }}</th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in data %}
                <tr>
                    {% for col in columns %}
                    <td>{{ row[col] }}</td>
                    {% endfor %}
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <h2>Sentiment Distribution for Top Posts</h2>
        <canvas id="sentimentDistributionChart"></canvas>

        <h2>Top Posts by Interactions</h2>
        <canvas id="topPostsByInteractionsChart"></canvas>

        <script>
            $(document).ready(function() {
                $('#topPostsTable').DataTable();

                var ctx2 = document.getElementById('sentimentDistributionChart').getContext('2d');
                new Chart(ctx2, {
                    type: 'bar',
                    data: {
                        labels: {{ sentiment_distribution.labels | safe }},
                        datasets: [{
                            label: 'Sentiment Score',
                            data: {{ sentiment_distribution.labels | safe }},
                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            x: { 
                                title: { display: true, text: 'Sentiment Score' }
                            },
                            y: { 
                                title: { display: true, text: 'Count' }
                            }
                        }
                    }
                });

                var ctx3 = document.getElementById('topPostsByInteractionsChart').getContext('2d');
                new Chart(ctx3, {
                    type: 'bar',
                    data: {
                        labels: {{ top_posts_by_interactions.labels | safe }},
                        datasets: [{
                            label: 'Interactions in 24h',
                            data: {{ top_posts_by_interactions.data | safe }},
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            x: { 
                                title: { display: true, text: 'Post Title' }
                            },
                            y: { 
                                title: { display: true, text: 'Interactions in 24h' }
                            }
                        }
                    }
                });
            });
        </script>
    </body>
    </html>
    """

    # Prepare data for templates
    columns = df.columns.tolist()
    data = df.to_dict(orient='records')

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(
        columns=columns, 
        data=data,
        sentiment_distribution=sentiment_distribution,
        top_posts_by_interactions=top_posts_by_interactions
    )

    # Save the generated HTML to a file
    with open(os.path.join('charts', 'top_posts_charts.html'), 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    df_top_posts = process_top_posts()
    generate_top_posts_charts(df_top_posts)
