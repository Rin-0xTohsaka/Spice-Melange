import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_topic_time_series():
    endpoint = "/public/topic/dogwifhat/time-series/v1"
    params = {"interval": "1w", "bucket": "hour"}
    data = fetch_data(endpoint, params=params)
    df = pd.DataFrame(data['data'])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def generate_topic_time_series_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Ensure the data is correctly formatted for Chart.js
    time_labels = df['time'].astype(str).tolist()
    interactions = df['interactions'].fillna(0).tolist()
    sentiment = df['sentiment'].fillna(0).tolist()
    posts_created = df['posts_created'].fillna(0).tolist()
    posts_active = df['posts_active'].fillna(0).tolist()
    contributors_created = df['contributors_created'].fillna(0).tolist()
    contributors_active = df['contributors_active'].fillna(0).tolist()

    # Debugging: print first few data points
    print("Time Labels:", time_labels[:5])
    print("Interactions Data:", interactions[:5])
    print("Sentiment Data:", sentiment[:5])
    print("Posts Created Data:", posts_created[:5])
    print("Posts Active Data:", posts_active[:5])
    print("Contributors Created Data:", contributors_created[:5])
    print("Contributors Active Data:", contributors_active[:5])

    # HTML Template for Chart.js with date formatting
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Topic Time Series</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
        <script src="https://cdn.jsdelivr.net/npm/date-fns@2.29.1/dist/date-fns.min.js"></script>
    </head>
    <body>
        <h1>Interactions Over Time</h1>
        <canvas id="interactionsOverTimeChart"></canvas>
        <script>
            var ctx = document.getElementById('interactionsOverTimeChart').getContext('2d');
            var interactionsOverTimeChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [{
                        label: 'Interactions',
                        data: {{ interactions | safe }},
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {
                    scales: {
                        x: { 
                            type: 'time',
                            time: {
                                unit: 'day',
                                tooltipFormat: 'yyyy-MM-dd',
                                displayFormats: {
                                    day: 'yyyy-MM-dd'
                                }
                            },
                            title: { display: true, text: 'Date' }
                        },
                        y: { 
                            title: { display: true, text: 'Interactions' }
                        }
                    }
                }
            });
        </script>

        <h1>Sentiment Over Time</h1>
        <canvas id="sentimentOverTimeChart"></canvas>
        <script>
            var ctx2 = document.getElementById('sentimentOverTimeChart').getContext('2d');
            var sentimentOverTimeChart = new Chart(ctx2, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [{
                        label: 'Sentiment',
                        data: {{ sentiment | safe }},
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {
                    scales: {
                        x: { 
                            type: 'time',
                            time: {
                                unit: 'day',
                                tooltipFormat: 'yyyy-MM-dd',
                                displayFormats: {
                                    day: 'yyyy-MM-dd'
                                }
                            },
                            title: { display: true, text: 'Date' }
                        },
                        y: { 
                            title: { display: true, text: 'Sentiment' }
                        }
                    }
                }
            });
        </script>

        <h1>Posts Created Over Time</h1>
        <canvas id="postsCreatedOverTimeChart"></canvas>
        <script>
            var ctx3 = document.getElementById('postsCreatedOverTimeChart').getContext('2d');
            var postsCreatedOverTimeChart = new Chart(ctx3, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [{
                        label: 'Posts Created',
                        data: {{ posts_created | safe }},
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {
                    scales: {
                        x: { 
                            type: 'time',
                            time: {
                                unit: 'day',
                                tooltipFormat: 'yyyy-MM-dd',
                                displayFormats: {
                                    day: 'yyyy-MM-dd'
                                }
                            },
                            title: { display: true, text: 'Date' }
                        },
                        y: { 
                            title: { display: true, text: 'Posts Created' }
                        }
                    }
                }
            });
        </script>

        <h1>Posts Active Over Time</h1>
        <canvas id="postsActiveOverTimeChart"></canvas>
        <script>
            var ctx4 = document.getElementById('postsActiveOverTimeChart').getContext('2d');
            var postsActiveOverTimeChart = new Chart(ctx4, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [{
                        label: 'Posts Active',
                        data: {{ posts_active | safe }},
                        borderColor: 'rgba(153, 102, 255, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {
                    scales: {
                        x: { 
                            type: 'time',
                            time: {
                                unit: 'day',
                                tooltipFormat: 'yyyy-MM-dd',
                                displayFormats: {
                                    day: 'yyyy-MM-dd'
                                }
                            },
                            title: { display: true, text: 'Date' }
                        },
                        y: { 
                            title: { display: true, text: 'Posts Active' }
                        }
                    }
                }
            });
        </script>

        <h1>Contributors Created Over Time</h1>
        <canvas id="contributorsCreatedOverTimeChart"></canvas>
        <script>
            var ctx5 = document.getElementById('contributorsCreatedOverTimeChart').getContext('2d');
            var contributorsCreatedOverTimeChart = new Chart(ctx5, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [{
                        label: 'Contributors Created',
                        data: {{ contributors_created | safe }},
                        borderColor: 'rgba(255, 206, 86, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {
                    scales: {
                        x: { 
                            type: 'time',
                            time: {
                                unit: 'day',
                                tooltipFormat: 'yyyy-MM-dd',
                                displayFormats: {
                                    day: 'yyyy-MM-dd'
                                }
                            },
                            title: { display: true, text: 'Date' }
                        },
                        y: { 
                            title: { display: true, text: 'Contributors Created' }
                        }
                    }
                }
            });
        </script>

        <h1>Contributors Active Over Time</h1>
        <canvas id="contributorsActiveOverTimeChart"></canvas>
        <script>
            var ctx6 = document.getElementById('contributorsActiveOverTimeChart').getContext('2d');
            var contributorsActiveOverTimeChart = new Chart(ctx6, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [{
                        label: 'Contributors Active',
                        data: {{ contributors_active | safe }},
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {
                    scales: {
                        x: { 
                            type: 'time',
                            time: {
                                unit: 'day',
                                tooltipFormat: 'yyyy-MM-dd',
                                displayFormats: {
                                    day: 'yyyy-MM-dd'
                                }
                            },
                            title: { display: true, text: 'Date' }
                        },
                        y: { 
                            title: { display: true, text: 'Contributors Active' }
                        }
                    }
                }
            });
        </script>

    </body>
    </html>
    """

    # Prepare data for templates
    data = {
        "time": time_labels,
        "interactions": interactions,
        "sentiment": sentiment,
        "posts_created": posts_created,
        "posts_active": posts_active,
        "contributors_created": contributors_created,
        "contributors_active": contributors_active
    }

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(data)

    # Save the generated HTML to a file
    with open(os.path.join('charts', 'topic_time_series.html'), 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    df_topic_time_series = process_topic_time_series()
    generate_topic_time_series_charts(df_topic_time_series)
