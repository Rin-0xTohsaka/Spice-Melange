import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_market_data():
    endpoint = "/public/coins/wif/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame([data['data']])
    df = df.applymap(lambda x: f'{x:.2f}' if isinstance(x, float) else x)  # Ensure two decimal places
    return df

def generate_market_data_charts(df):
    os.makedirs('charts', exist_ok=True)

    # HTML Template for DataTables
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Market Data</title>
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.css">
        <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.5.1.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.js"></script>
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
                bottom: 125%; /* Position the tooltip above the text */
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
        <h1>Market Data</h1>
        <table id="marketDataTable" class="display">
            <thead>
                <tr>
                    <th>Market Cap (USD)</th>
                    <th>Price (USD)</th>
                    <th>24h Volume (USD)</th>
                    <th>24h % Change</th>
                    <th>7d % Change</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>${{ market_cap }}</td>
                    <td>${{ price }}</td>
                    <td>${{ volume_24h }}</td>
                    <td>{{ percent_change_24h }}%</td>
                    <td>{{ percent_change_7d }}%</td>
                </tr>
            </tbody>
        </table>
        <script>
            $(document).ready(function() {
                $('#marketDataTable').DataTable();
            });
        </script>
    </body>
    </html>
    """

    # Prepare data for templates
    data = {
        "market_cap": df['market_cap'][0],
        "price": df['price'][0],
        "volume_24h": df['volume_24h'][0],
        "percent_change_24h": df['percent_change_24h'][0],
        "percent_change_7d": df['percent_change_7d'][0]
    }

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**data)

    # Save HTML to file
    with open(os.path.join('charts', 'market_data.html'), 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    df_market_data = process_market_data()
    generate_market_data_charts(df_market_data)
