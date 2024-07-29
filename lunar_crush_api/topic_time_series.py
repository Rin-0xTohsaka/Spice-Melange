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
    interactions = df['interactions'].tolist()
    sentiment = df['sentiment'].tolist()
    posts_created = df['posts_created'].tolist()
    posts_active = df['posts_active'].tolist()
    contributors_created = df['contributors_created'].tolist()
    contributors_active = df['contributors_active'].tolist()
    
    # HTML Template for Chart.js with debugging information
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Topic Time Series</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            .tooltip {
                position: relative;
                display: inline-block;
                cursor: pointer;
            }
            .tooltip .tooltiptext {
                visibility: hidden;
                width: 200px;
                background-color: black;
                color: #fff;
                text-align: center;
                border-radius: 6px;
                padding: 5px;
                position: absolute;
                z-index: 1;
                bottom: 125%;
                left: 50%;
                margin-left: -100px;
                opacity: 0;
                transition: opacity 0.3s;
            }
            .tooltip:hover .tooltiptext {
                visibility: visible;
                opacity: 1;
            }
        </style>
    </head>
    <body>
        <h1>Topic Time Series Data</h1>
        
        <div class="tooltip">Interactions Over Time
            <span class="tooltiptext">Total number of publicly measurable engagements on posts over time.</span>
        </div>
        <canvas id="interactionsOverTimeChart"></canvas>
        <script>
            console.log('Time Labels: ', {{ time | safe }});
            console.log('Interactions Data: ', {{ interactions | safe }});
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
                                unit: 'hour'
                            },
                            title: { display: true, text: 'Time' }
                        },
                        y: { 
                            title: { display: true, text: 'Interactions' }
                        }
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.dataset.label + ': ' + context.raw.toLocaleString();
                                }
                            }
                        }
                    }
                }
            });
        </script>

        <div class="tooltip">Sentiment Over Time
            <span class="tooltiptext">Sentiment scores of posts over time.</span>
        </div>
        <canvas id="sentimentOverTimeChart"></canvas>
        <script>
            console.log('Sentiment Data: ', {{ sentiment | safe }});
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
                                unit: 'hour'
                            },
                            title: { display: true, text: 'Time' }
                        },
                        y: { 
                            title: { display: true, text: 'Sentiment' }
                        }
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.dataset.label + ': ' + context.raw.toLocaleString();
                                }
                            }
                        }
                    }
                }
            });
        </script>

        <div class="tooltip">Post and Contributor Activity Over Time
            <span class="tooltiptext">Number of posts and active contributors over time.</span>
        </div>
        <canvas id="postContributorActivityChart"></canvas>
        <script>
            console.log('Posts Created Data: ', {{ posts_created | safe }});
            console.log('Posts Active Data: ', {{ posts_active | safe }});
            console.log('Contributors Created Data: ', {{ contributors_created | safe }});
            console.log('Contributors Active Data: ', {{ contributors_active | safe }});
            var ctx3 = document.getElementById('postContributorActivityChart').getContext('2d');
            var postContributorActivityChart = new Chart(ctx3, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [
                        { label: 'Posts Created', data: {{ posts_created | safe }}, borderColor: 'rgba(255, 99, 132, 1)', borderWidth: 2, fill: false },
                        { label: 'Posts Active', data: {{ posts_active | safe }}, borderColor: 'rgba(54, 162, 235, 1)', borderWidth: 2, fill: false },
                        { label: 'Contributors Created', data: {{ contributors_created | safe }}, borderColor: 'rgba(75, 192, 192, 1)', borderWidth: 2, fill: false },
                        { label: 'Contributors Active', data: {{ contributors_active | safe }}, borderColor: 'rgba(153, 102, 255, 1)', borderWidth: 2, fill: false }
                    ]
                },
                options: {
                    scales: {
                        x: { 
                            type: 'time',
                            time: {
                                unit: 'hour'
                            },
                            title: { display: true, text: 'Time' }
                        },
                        y: { 
                            title: { display: true, text: 'Activity Count' }
                        }
                    },
                    plugins: {
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.dataset.label + ': ' + context.raw.toLocaleString();
                                }
                            }
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

    # Debugging: print data to ensure correct format
    print(data)

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**data)

    # Save HTML to file
    with open(os.path.join('charts', 'topic_time_series.html'), 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    df_topic_time_series = process_topic_time_series()
    generate_topic_time_series_charts(df_topic_time_series)
