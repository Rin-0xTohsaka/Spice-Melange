import os
import time
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_coin_data(coin):
    endpoint = f"/public/coins/{coin}/time-series/v2"
    params = {"interval": "1w", "bucket": "hour"}
    data = fetch_data(endpoint, params=params)

    if 'data' not in data:
        print(f"Warning: 'data' key not found for coin {coin}")
        return pd.DataFrame()  # Return an empty DataFrame if data is not present

    df = pd.DataFrame(data['data'])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['coin'] = coin  # Add a column to identify the coin
    return df

def generate_comparison_charts(coins):
    os.makedirs('charts', exist_ok=True)
    
    all_data = pd.DataFrame()

    # Fetch and combine data for all coins with a delay to avoid rate limiting
    for coin in coins:
        coin_data = process_coin_data(coin)
        if not coin_data.empty:
            all_data = pd.concat([all_data, coin_data], ignore_index=True)
        time.sleep(10)  # Adjust the delay as needed
    
    if all_data.empty:
        print("No data available for the given coins.")
        return
    
    # Convert 'time' column to string for JSON serialization
    all_data['time'] = all_data['time'].astype(str)

    # HTML Template for Chart.js with datetime formatting
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Coin Comparison</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
    </head>
    <body>
        <h1>Market Cap Comparison</h1>
        <canvas id="marketCapComparisonChart"></canvas>
        <h1>Volume Comparison</h1>
        <canvas id="volumeComparisonChart"></canvas>
        <h1>Social Dominance Comparison</h1>
        <canvas id="socialDominanceComparisonChart"></canvas>
        <h1>Volatility Comparison</h1>
        <canvas id="volatilityComparisonChart"></canvas>
        <script>
            const data = {{ all_data | tojson | safe }};

            function prepareData(data, metric) {
                const result = {};
                data.forEach(item => {
                    if (!result[item.coin]) {
                        result[item.coin] = { labels: [], data: [] };
                    }
                    result[item.coin].labels.push(new Date(item.time));
                    result[item.coin].data.push(item[metric]);
                });
                return result;
            }

            function createChart(ctx, data, label, metric) {
                const datasets = Object.keys(data).map(coin => ({
                    label: coin,
                    data: data[coin].data,
                    borderColor: `rgba(${Math.random()*255}, ${Math.random()*255}, ${Math.random()*255}, 1)`,
                    borderWidth: 2,
                    fill: false
                }));

                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data[Object.keys(data)[0]].labels,
                        datasets: datasets
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
                            y: { title: { display: true, text: label }}
                        }
                    }
                });
            }

            const marketCapData = prepareData(data, 'market_cap');
            createChart(document.getElementById('marketCapComparisonChart').getContext('2d'), marketCapData, 'Market Cap (USD)');

            const volumeData = prepareData(data, 'volume_24h');
            createChart(document.getElementById('volumeComparisonChart').getContext('2d'), volumeData, '24h Volume (USD)');

            const socialDominanceData = prepareData(data, 'social_dominance');
            createChart(document.getElementById('socialDominanceComparisonChart').getContext('2d'), socialDominanceData, 'Social Dominance (%)');

            const volatilityData = prepareData(data, 'volatility');
            createChart(document.getElementById('volatilityComparisonChart').getContext('2d'), volatilityData, 'Volatility');
        </script>
    </body>
    </html>
    """

    # Prepare data for template
    data = all_data.to_dict(orient='records')

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(all_data=data)

    # Save HTML to file
    with open(os.path.join('charts', 'coin_comparison.html'), 'w') as f:
        f.write(html_content)

    print("Comparison charts generated successfully.")
