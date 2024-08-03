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

def generate_chart_html(df, chart_id, chart_label, metric, x_label, y_label, file_name):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ chart_label }}</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
        <link rel="stylesheet" href="styles.css">
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

                const darkModeMediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
                function updateChartColors(chart) {
                    const mode = darkModeMediaQuery.matches ? 'dark' : 'light';
                    const textColor = mode === 'dark' ? '#FFFFFF' : '#000000';
                    chart.options.scales.x.title.color = textColor;
                    chart.options.scales.y.title.color = textColor;
                    chart.options.scales.x.ticks.color = textColor;
                    chart.options.scales.y.ticks.color = textColor;
                    chart.options.plugins.legend.labels.color = textColor;
                    chart.update();
                }
                darkModeMediaQuery.addEventListener('change', () => {
                    updateChartColors(chart);
                });

                var ctx = canvas.getContext('2d');
                var chart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: {{ time | safe }},
                        datasets: [{
                            label: '{{ metric }}',
                            data: {{ data | safe }},
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
                                title: { display: true, text: '{{ x_label }}' }
                            },
                            y: { 
                                title: { display: true, text: '{{ y_label }}' }
                            }
                        },
                        plugins: {
                            zoom: {
                                zoom: {
                                    wheel: { enabled: true },
                                    pinch: { enabled: true },
                                    mode: 'x'
                                },
                                pan: {
                                    enabled: true,
                                    mode: 'x'
                                }
                            },
                            legend: {
                                labels: {
                                    color: '#000000' // Default color
                                }
                            }
                        }
                    }
                });
                updateChartColors(chart);
            });
        </script>
    </body>
    </html>
    """

    # Prepare data for the template
    template_data = {
        "time": df['time'].astype(str).tolist(),  # Convert to string format
        "chart_id": chart_id,
        "chart_label": chart_label,
        "metric": metric,
        "x_label": x_label,
        "y_label": y_label,
        "data": df[metric].tolist()
    }

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**template_data)

    # Save HTML to file
    with open(os.path.join('charts', file_name), 'w') as f:
        f.write(html_content)

def generate_topic_time_series_charts(df):
    os.makedirs('charts', exist_ok=True)

    generate_chart_html(
        df=df,
        chart_id="interactionsOverTimeChart",
        chart_label="Interactions Over Time",
        metric="interactions",
        x_label="Date",
        y_label="Interactions",
        file_name="interactions_over_time.html"
    )

    generate_chart_html(
        df=df,
        chart_id="sentimentOverTimeChart",
        chart_label="Sentiment Over Time",
        metric="sentiment",
        x_label="Date",
        y_label="Sentiment",
        file_name="sentiment_over_time.html"
    )

    generate_chart_html(
        df=df,
        chart_id="postsCreatedOverTimeChart",
        chart_label="Posts Created Over Time",
        metric="posts_created",
        x_label="Date",
        y_label="Posts Created",
        file_name="posts_created_over_time.html"
    )

    generate_chart_html(
        df=df,
        chart_id="postsActiveOverTimeChart",
        chart_label="Posts Active Over Time",
        metric="posts_active",
        x_label="Date",
        y_label="Posts Active",
        file_name="posts_active_over_time.html"
    )

    generate_chart_html(
        df=df,
        chart_id="contributorsCreatedOverTimeChart",
        chart_label="Contributors Created Over Time",
        metric="contributors_created",
        x_label="Date",
        y_label="Contributors Created",
        file_name="contributors_created_over_time.html"
    )

    generate_chart_html(
        df=df,
        chart_id="contributorsActiveOverTimeChart",
        chart_label="Contributors Active Over Time",
        metric="contributors_active",
        x_label="Date",
        y_label="Contributors Active",
        file_name="contributors_active_over_time.html"
    )

if __name__ == "__main__":
    df_topic_time_series = process_topic_time_series()
    generate_topic_time_series_charts(df_topic_time_series)
