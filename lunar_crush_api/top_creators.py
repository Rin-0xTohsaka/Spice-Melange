import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_top_creators():
    endpoint = "/public/topic/dogwifhat/creators/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame(data['data'])
    return df

def generate_top_creators_charts(df):
    os.makedirs('charts', exist_ok=True)

    # HTML Template for Chart.js
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Top Creators</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <h1>Top Creators Table</h1>
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

        <h1>Interactions in Last 24 Hours by Creator</h1>
        <canvas id="interactions24hChart"></canvas>
        <script>
            var ctx = document.getElementById('interactions24hChart').getContext('2d');
            var interactions24hChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: {{ creator_names | safe }},
                    datasets: [{
                        label: 'Interactions (24h)',
                        data: {{ interactions_24h | safe }},
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        x: { title: { display: true, text: 'Creator Name' }},
                        y: { title: { display: true, text: 'Interactions (24h)' }}
                    }
                }
            });
        </script>

        <h1>Follower Count Distribution</h1>
        <canvas id="followerCountChart"></canvas>
        <script>
            var ctx2 = document.getElementById('followerCountChart').getContext('2d');
            var followerCountChart = new Chart(ctx2, {
                type: 'bar',
                data: {
                    labels: {{ creator_names | safe }},
                    datasets: [{
                        label: 'Number of Followers',
                        data: {{ creator_followers | safe }},
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        x: { title: { display: true, text: 'Creator Name' }},
                        y: { title: { display: true, text: 'Number of Followers' }}
                    }
                }
            });
        </script>

        <h1>Number of Posts in Last 24 Hours by Creator</h1>
        <canvas id="postActivityChart"></canvas>
        <script>
            var ctx3 = document.getElementById('postActivityChart').getContext('2d');
            var postActivityChart = new Chart(ctx3, {
                type: 'bar',
                data: {
                    labels: {{ creator_names | safe }},
                    datasets: [{
                        label: 'Posts (24h)',
                        data: {{ creator_posts | safe }},
                        backgroundColor: 'rgba(153, 102, 255, 0.2)',
                        borderColor: 'rgba(153, 102, 255, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        x: { title: { display: true, text: 'Creator Name' }},
                        y: { title: { display: true, text: 'Posts (24h)' }}
                    }
                }
            });
        </script>
    </body>
    </html>
    """

    # Prepare data for templates
    data = {
        "columns": df.columns.tolist(),
        "data": df.values.tolist(),
        "creator_names": df['creator_name'].tolist(),
        "interactions_24h": df['interactions_24h'].tolist(),
        "creator_followers": df['creator_followers'].tolist(),
        "creator_posts": df['creator_posts'].tolist()
    }

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**data)

    # Save HTML to file
    with open(os.path.join('charts', 'top_creators.html'), 'w') as f:
        f.write(html_content)
