# gecko_terminal_api/pools_data.py

import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data
from .endpoints import BASE_URL, endpoints

def format_decimal(value):
    try:
        return f"{float(value):.2f}"
    except (ValueError, TypeError):
        return value

def process_pools_data():
    endpoint = endpoints["pools_data"]
    params = {
        "page": 1,
        "sort": "h24_volume_usd_desc"
    }
    data = fetch_data(BASE_URL + endpoint, params=params)

    # Extract relevant fields
    pools = []
    for pool in data['data']:
        attributes = pool['attributes']
        dex = pool['relationships']['dex']['data']['id']
        pools.append({
            "DEX": dex,
            "Pool ID": pool['id'],
            "Type": pool['type'],
            "Base Token Price (USD)": format_decimal(attributes['base_token_price_usd']),
            "Quote Token Price (USD)": format_decimal(attributes['quote_token_price_usd']),
            "Pair Name (Base/Quote)": attributes['name'],
            "Token Price (USD)": format_decimal(attributes.get('token_price_usd', 'N/A')),
            "FDV (USD)": format_decimal(attributes.get('fdv_usd', 'N/A')),
            "Market Cap (USD)": format_decimal(attributes.get('market_cap_usd', 'N/A')),
            "Price Change (24h)": format_decimal(attributes['price_change_percentage'].get('h24', 'N/A')),
            "Transactions (24h) Buys": attributes['transactions']['h24'].get('buys', 'N/A'),
            "Transactions (24h) Sells": attributes['transactions']['h24'].get('sells', 'N/A'),
            "Volume (24h) USD": format_decimal(attributes['volume_usd'].get('h24', 'N/A')),
            "Reserve (USD)": format_decimal(attributes.get('reserve_in_usd', 'N/A')),
        })
    
    df = pd.DataFrame(pools)
    return df

def generate_pools_data_charts(df):
    os.makedirs('charts', exist_ok=True)

    # HTML Template for DataTables
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pools Data</title>
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.css">
        <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.5.1.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.js"></script>
    </head>
    <body>
        <h1>Pools Data Table</h1>
        <table id="poolsTable" class="display">
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
        <script>
            $(document).ready( function () {
                $('#poolsTable').DataTable();
            });
        </script>
    </body>
    </html>
    """

    # Prepare data for templates
    data = {
        "columns": df.columns.tolist(),
        "data": df.values.tolist()
    }

    # Render HTML with data
    template = Template(html_template)
    html_content = template.render(**data)

    # Save HTML to file
    with open(os.path.join('charts', 'pools_data.html'), 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    df_pools_data = process_pools_data()
    generate_pools_data_charts(df_pools_data)
