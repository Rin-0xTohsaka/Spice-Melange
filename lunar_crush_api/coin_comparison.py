import os
import time
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_coin_data(coin):
    endpoint = f"/public/coins/{coin}/time-series/v2"
    params = {
        "bucket": "day",
        "interval": "1d",
        "start": 1704171600,
        "end": 1733115600
    }
    data = fetch_data(endpoint, params=params)

    if 'data' not in data:
        print(f"Warning: 'data' key not found for coin {coin}")
        return pd.DataFrame()  # Return an empty DataFrame if data is not present

    df = pd.DataFrame(data['data'])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['coin'] = coin  # Add a column to identify the coin
    return df

def generate_chart_html(data, chart_id, chart_label, metric, x_label, y_label, file_name):
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
        <link rel="stylesheet" href="styles.css">
        <style>
            canvas {
                max-width: 800px; /* Adjust this value to change the width */
                max-height: 500px; /* Adjust this value to change the height */
            }
        </style>
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

                const data = {{ all_data | tojson | safe }};
                const preparedData = prepareData(data, '{{ metric }}');
                const datasets = Object.keys(preparedData).map(coin => ({
                    label: coin,
                    data: preparedData[coin].data,
                    borderColor: `rgba(${Math.random()*255}, ${Math.random()*255}, ${Math.random()*255}, 1)`,
                    borderWidth: 2,
                    fill: false
                }));

                var ctx = document.getElementById('{{ chart_id }}').getContext('2d');
                var chart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: preparedData[Object.keys(preparedData)[0]].labels,
                        datasets: datasets
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
    template_data = {
        "all_data": data,
        "chart_id": chart_id,
        "chart_label": chart_label,
        "metric": metric,
        "x_label": x_label,
        "y_label": y_label
    }

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**template_data)

    # Save HTML to file
    with open(os.path.join('charts', file_name), 'w') as f:
        f.write(html_content)

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

    # Generate each chart on its own HTML page
    generate_chart_html(
        data=all_data.to_dict(orient='records'),
        chart_id="marketCapComparisonChart",
        chart_label="Market Cap Comparison",
        metric="market_cap",
        x_label="Date",
        y_label="Market Cap (USD)",
        file_name="market_cap_comparison.html"
    )

    generate_chart_html(
        data=all_data.to_dict(orient='records'),
        chart_id="volumeComparisonChart",
        chart_label="Volume Comparison",
        metric="volume_24h",
        x_label="Date",
        y_label="24h Volume (USD)",
        file_name="volume_comparison.html"
    )

    generate_chart_html(
        data=all_data.to_dict(orient='records'),
        chart_id="socialDominanceComparisonChart",
        chart_label="Social Dominance Comparison",
        metric="social_dominance",
        x_label="Date",
        y_label="Social Dominance (%)",
        file_name="social_dominance_comparison.html"
    )

    generate_chart_html(
        data=all_data.to_dict(orient='records'),
        chart_id="volatilityComparisonChart",
        chart_label="Volatility Comparison",
        metric="volatility",
        x_label="Date",
        y_label="Volatility",
        file_name="volatility_comparison.html"
    )

    print("Comparison charts generated successfully.")
