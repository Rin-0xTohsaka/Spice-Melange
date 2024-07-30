import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_market_time_series():
    endpoint = "/public/coins/wif/time-series/v2"
    params = {
        "bucket": "day",
        "interval": "1d",
        "start": 1704171600,
        "end": 1733115600
    }
    data = fetch_data(endpoint, params=params)
    df = pd.DataFrame(data['data'])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def validate_data(df, columns):
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0)
    return df

def generate_chart_html(df, chart_id, chart_label, chart_data, x_label, y_label, file_name):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ chart_label }}</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>
        <link rel="stylesheet" href="../styles.css">
    </head>
    <body>
        <h1>{{ chart_label }}</h1>
        <canvas id="{{ chart_id }}"></canvas>

        <script>
            document.addEventListener('DOMContentLoaded', function() {
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

                var ctx = document.getElementById('{{ chart_id }}').getContext('2d');
                var chart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: {{ time | safe }},
                        datasets: {{ chart_data | safe }}
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
                            y: { title: { display: true, text: '{{ y_label }}' }}
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
    data = {
        "time": df['time'].astype(str).tolist(),  # Ensure the time is in string format
        "chart_label": chart_label,
        "chart_data": chart_data,
        "x_label": x_label,
        "y_label": y_label,
        "chart_id": chart_id
    }

    # Convert boolean values to JavaScript-compatible strings
    data["chart_data"] = str(data["chart_data"]).replace("False", "false").replace("True", "true")

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**data)

    # Save HTML to file
    with open(os.path.join('charts', file_name), 'w') as f:
        f.write(html_content)

def generate_market_time_series_charts(df):
    os.makedirs('charts', exist_ok=True)

    # Validate and clean the data
    columns_to_validate = ['market_cap', 'open', 'close', 'high', 'low', 'volume_24h']
    df = validate_data(df, columns_to_validate)

    # Generate each chart on its own HTML page
    generate_chart_html(
        df=df,
        chart_id="marketCapOverTimeChart",
        chart_label="Market Cap Over Time",
        chart_data=[{
            'label': 'Market Cap',
            'data': df['market_cap'].tolist(),
            'borderColor': 'rgba(54, 162, 235, 1)',
            'borderWidth': 2,
            'fill': False
        }],
        x_label="Date",
        y_label="Market Cap (USD)",
        file_name="market_cap_over_time.html"
    )

    generate_chart_html(
        df=df,
        chart_id="priceMovementOverTimeChart",
        chart_label="Price Movement Over Time",
        chart_data=[
            {'label': 'Open', 'data': df['open'].tolist(), 'borderColor': 'rgba(255, 99, 132, 1)', 'borderWidth': 2, 'fill': False},
            {'label': 'Close', 'data': df['close'].tolist(), 'borderColor': 'rgba(54, 162, 235, 1)', 'borderWidth': 2, 'fill': False},
            {'label': 'High', 'data': df['high'].tolist(), 'borderColor': 'rgba(75, 192, 192, 1)', 'borderWidth': 2, 'fill': False},
            {'label': 'Low', 'data': df['low'].tolist(), 'borderColor': 'rgba(153, 102, 255, 1)', 'borderWidth': 2, 'fill': False}
        ],
        x_label="Date",
        y_label="Price (USD)",
        file_name="price_movement_over_time.html"
    )

    generate_chart_html(
        df=df,
        chart_id="volumeMarketCapOverTimeChart",
        chart_label="Volume and Market Cap Over Time",
        chart_data=[
            {'label': '24h Volume', 'data': df['volume_24h'].tolist(), 'borderColor': 'rgba(255, 159, 64, 1)', 'borderWidth': 2, 'fill': False},
            {'label': 'Market Cap', 'data': df['market_cap'].tolist(), 'borderColor': 'rgba(54, 162, 235, 1)', 'borderWidth': 2, 'fill': False}
        ],
        x_label="Date",
        y_label="USD",
        file_name="volume_market_cap_over_time.html"
    )

if __name__ == "__main__":
    df_market_time_series = process_market_time_series()
    generate_market_time_series_charts(df_market_time_series)
