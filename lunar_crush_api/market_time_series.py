import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_market_time_series():
    endpoint = "/public/coins/wif/time-series/v2"
    params = {"interval": "1w", "bucket": "hour"}
    data = fetch_data(endpoint, params=params)
    df = pd.DataFrame(data['data'])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def generate_market_time_series_charts(df):
    os.makedirs('charts', exist_ok=True)
    
    # HTML Template for Chart.js with datetime formatting
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Market Time Series</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
    </head>
    <body>
        <h1>Market Cap Over Time</h1>
        <canvas id="marketCapOverTimeChart"></canvas>
        <script>
            var ctx = document.getElementById('marketCapOverTimeChart').getContext('2d');
            var marketCapOverTimeChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [{
                        label: 'Market Cap',
                        data: {{ market_cap | safe }},
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
                        y: { title: { display: true, text: 'Market Cap (USD)' }}
                    }
                }
            });
        </script>

        <h1>Price Movement Over Time</h1>
        <canvas id="priceMovementOverTimeChart"></canvas>
        <script>
            var ctx2 = document.getElementById('priceMovementOverTimeChart').getContext('2d');
            var priceMovementOverTimeChart = new Chart(ctx2, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [
                        { label: 'Open', data: {{ open | safe }}, borderColor: 'rgba(255, 99, 132, 1)', borderWidth: 2, fill: false },
                        { label: 'Close', data: {{ close | safe }}, borderColor: 'rgba(54, 162, 235, 1)', borderWidth: 2, fill: false },
                        { label: 'High', data: {{ high | safe }}, borderColor: 'rgba(75, 192, 192, 1)', borderWidth: 2, fill: false },
                        { label: 'Low', data: {{ low | safe }}, borderColor: 'rgba(153, 102, 255, 1)', borderWidth: 2, fill: false }
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
                        y: { title: { display: true, text: 'Price (USD)' }}
                    }
                }
            });
        </script>

        <h1>Volume and Market Cap Over Time</h1>
        <canvas id="volumeMarketCapOverTimeChart"></canvas>
        <script>
            var ctx3 = document.getElementById('volumeMarketCapOverTimeChart').getContext('2d');
            var volumeMarketCapOverTimeChart = new Chart(ctx3, {
                type: 'line',
                data: {
                    labels: {{ time | safe }},
                    datasets: [
                        { label: '24h Volume', data: {{ volume_24h | safe }}, borderColor: 'rgba(255, 159, 64, 1)', borderWidth: 2, fill: false },
                        { label: 'Market Cap', data: {{ market_cap | safe }}, borderColor: 'rgba(54, 162, 235, 1)', borderWidth: 2, fill: false }
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
                        y: { title: { display: true, text: 'USD' }}
                    }
                }
            });
        </script>
    </body>
    </html>
    """

    # Prepare data for templates
    data = {
        "time": df['time'].astype(str).tolist(),  # Ensure the time is in string format
        "market_cap": df['market_cap'].tolist(),
        "open": df['open'].tolist(),
        "close": df['close'].tolist(),
        "high": df['high'].tolist(),
        "low": df['low'].tolist(),
        "volume_24h": df['volume_24h'].tolist()
    }

    print("Data prepared for template rendering:")
    print(data)  # Logging the data prepared for the template

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**data)

    # Save HTML to file
    with open(os.path.join('charts', 'market_time_series.html'), 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    df_market_time_series = process_market_time_series()
    generate_market_time_series_charts(df_market_time_series)
