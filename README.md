# spice-melange
Awareness spectrum narcotic for meme communities on Notion 

## Project Goals
1. Query data from the LunarCrush API.
2. Generate various charts from the queried data.
3. Render the charts on a Notion dashboard.
4. Automate the process to ensure the dashboard is always up-to-date.

## System Architecture

### Components:
1. **API Query Script**: A script to fetch data from the LunarCrush API.
2. **Data Processing**: Transform the data into a format suitable for charting.
3. **Chart Generation**: Create charts using a charting library.
4. **Hosting**: Host the charts online.
5. **Notion Integration**: Embed the charts into a Notion page.
6. **Automation**: Use cron jobs to automate the data fetching and chart generation process.

## Detailed Steps

### 1. API Query Script
- **Language**: Python
- **Library**: `requests` for making HTTP requests.

**Example Code**:
```python
import requests

api_url = "https://lunarcrush.com/api4/public/coins/dogwifhat/time-series/v1"
headers = {
    "Authorization": "Bearer <YourAPIToken>"
}

response = requests.get(api_url, headers=headers)
data = response.json()
```

### 2. Data Processing
- **Library**: `pandas` for data manipulation.

**Example Code**:
```python
import pandas as pd

# Process the data into a DataFrame
df = pd.DataFrame(data['data'])
```

### 3. Chart Generation
- **Library**: `plotly` for interactive charts.

**Example Code**:
```python
import plotly.express as px

fig = px.line(df, x='timestamp', y='market_cap', title='Dogwifhat Market Cap')
fig.write_html('chart.html')
```

### 4. Hosting
- **Service**: GitHub Pages, Netlify, or any other static site hosting service.
- **Steps**:
  1. Upload the generated HTML files to the hosting service.
  2. Get the public URLs of the hosted charts.

### 5. Notion Integration
- **Steps**:
  1. Copy the URLs of the hosted charts.
  2. In Notion, type `/embed`.
  3. Paste the URL into the embed block.

### 6. Automation
- **Tool**: `cron` for scheduling tasks.
- **Library**: `schedule` for scheduling in Python.

**Example Code**:
```python
import schedule
import time

def job():
    # Fetch data
    response = requests.get(api_url, headers=headers)
    data = response.json()
    # Process and generate chart
    df = pd.DataFrame(data['data'])
    fig = px.line(df, x='timestamp', y='market_cap', title='Dogwifhat Market Cap')
    fig.write_html('/path/to/your/hosted/chart.html')
    # Upload to hosting service (depends on service API)

schedule.every().day.at("01:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## Libraries and Tools

1. **Python Libraries**:
   - `requests`: To query the LunarCrush API.
   - `pandas`: For data processing.
   - `plotly`: For chart generation.
   - `schedule`: For scheduling tasks in Python.
2. **Hosting Service**: GitHub Pages, Netlify, or similar.
3. **Notion**: For embedding the charts.

## Hosting Strategy
1. **Static Site Hosting**: Use GitHub Pages or Netlify to host the generated HTML files.
2. **Steps**:
   - Commit the HTML files to a GitHub repository.
   - Enable GitHub Pages for the repository or connect it to Netlify.
   - Use the public URLs for embedding in Notion.

## Full Spec Sheet

### Overview:
- Goal: Create a dynamic dashboard on Notion using data from LunarCrush API.
- Components: API Query Script, Data Processing, Chart Generation, Hosting, Notion Integration, Automation.

### System Architecture:
- API Query Script: Python with `requests`.
- Data Processing: Python with `pandas`.
- Chart Generation: Python with `plotly`.
- Hosting: GitHub Pages/Netlify.
- Notion Integration: Embed blocks.
- Automation: `cron` and `schedule`.

### Detailed Steps:
- Query data from LunarCrush API using `requests`.
- Process data using `pandas`.
- Generate charts using `plotly`.
- Host charts on GitHub Pages or Netlify.
- Embed charts in Notion.
- Automate using `cron` and `schedule`.

### Libraries and Tools:
- `requests`, `pandas`, `plotly`, `schedule`.
- GitHub Pages, Netlify.
- Notion.

### Hosting Strategy:
- Use GitHub Pages or Netlify for hosting.
- Public URLs for embedding in Notion.

### API Integration:
- Authentication: Use Bearer token.
- Endpoints: `/public/coins/dogwifhat/time-series/v1`, and other relevant endpoints for the required data.

### Data Points:
- Marketcap, Trading Volume, Circulating Supply, All Time High, 52-week low, 52-week high.
- Activity Summary data, Top creators data, Sentiment data, Sentiment by network data, Network popularity data, Posts data.

