import os
import pandas as pd
from jinja2 import Template
from .fetch_data import fetch_data

def process_top_creators():
    endpoint = "/public/topic/dogwifhat/creators/v1"
    data = fetch_data(endpoint)
    df = pd.DataFrame(data['data'])
    df = df.applymap(lambda x: f'{x:.2f}' if isinstance(x, float) else x)  # Ensure two decimal places
    return df

def generate_top_creators_charts(df):
    os.makedirs('charts', exist_ok=True)

    # HTML Template for DataTables
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Top Creators</title>
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.css">
        <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.5.1.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.js"></script>
    </head>
    <body>
        <h1>Top Creators Table</h1>
        <table id="topCreatorsTable" class="display">
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
            $(document).ready(function() {
                $('#topCreatorsTable').DataTable();
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
    with open(os.path.join('charts', 'top_creators.html'), 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    df_top_creators = process_top_creators()
    generate_top_creators_charts(df_top_creators)
