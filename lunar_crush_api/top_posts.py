import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_top_posts():
    endpoint = "/public/topic/dogwifhat/posts/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame(data['data'])
    return df

def generate_table_html(df):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Top Posts Table</title>
        <link rel="stylesheet" href="styles.css">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.25/css/jquery.dataTables.min.css">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>
    </head>
    <body>
        <h1>Top Posts Table</h1>
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
        <script>
            $(document).ready(function() {
                $('#topPostsTable').DataTable();
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
    html_content = template.render(columns=columns, data=data)

    # Save the generated HTML to a file
    with open(os.path.join('charts', 'top_posts_table.html'), 'w') as f:
        f.write(html_content)

def generate_chart_html(chart_data, chart_id, chart_label, x_label, y_label, file_name):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ chart_label }}</title>
        <link rel="stylesheet" href="styles.css">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <h1>{{ chart_label }}</h1>
        <canvas id="{{ chart_id }}" style="height: 400px;"></canvas>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const canvas = document.getElementById('{{ chart_id }}');

                // Adjust canvas height based on screen width
                if (window.innerWidth <= 768) {
                    canvas.style.height = '600px'; // Set taller height for mobile devices
                }

                var ctx = canvas.getContext('2d');
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: {{ chart_data.labels | safe }},
                        datasets: [{
                            label: '{{ y_label }}',
                            data: {{ chart_data.data | safe }},
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            x: { 
                                title: { display: true, text: '{{ x_label }}' }
                            },
                            y: { 
                                title: { display: true, text: '{{ y_label }}' }
                            }
                        }
                    }
                });
            });
        </script>
    </body>
    </html>
    """

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(chart_data=chart_data, chart_id=chart_id, chart_label=chart_label, x_label=x_label, y_label=y_label)

    # Save the generated HTML to a file
    with open(os.path.join('charts', file_name), 'w') as f:
        f.write(html_content)

def generate_top_posts_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Ensure the data is correctly formatted
    df['post_created'] = pd.to_datetime(df['post_created'], unit='s').astype(str)
    df['post_sentiment'] = df['post_sentiment'].fillna(0)
    df['interactions_24h'] = df['interactions_24h'].fillna(0)

    # Data for Chart.js
    sentiment_distribution = {
        'labels': df['post_sentiment'].tolist(),
        'data': df['post_sentiment'].tolist()
    }

    top_posts_by_interactions = {
        'labels': df['post_title'].tolist(),
        'data': df['interactions_24h'].tolist()
    }

    # Generate separate HTML files for the table and each chart
    generate_table_html(df)

    generate_chart_html(
        chart_data=sentiment_distribution,
        chart_id="sentimentDistributionChart",
        chart_label="Sentiment Distribution for Top Posts",
        x_label="Sentiment Score",
        y_label="Count",
        file_name="sentiment_distribution.html"
    )

    generate_chart_html(
        chart_data=top_posts_by_interactions,
        chart_id="topPostsByInteractionsChart",
        chart_label="Top Posts by Interactions",
        x_label="Post Title",
        y_label="Interactions in 24h",
        file_name="top_posts_by_interactions.html"
    )

if __name__ == "__main__":
    df_top_posts = process_top_posts()
    generate_top_posts_charts(df_top_posts)
