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

### 2. Data Processing
- **Library**: `pandas` for data manipulation.

### 3. Chart Generation
- **Library**: `plotly` for interactive charts.

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

## Libraries and Tools

1. **Python Libraries**:
   - `requests`: To query the LunarCrush API.
   - `pandas`: For data processing.
   - `plotly`: For chart generation.
   - `schedule`: For scheduling tasks in Python.
   - `wordcloud`: For generating word clouds.
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
- `requests`, `pandas`, `plotly`, `schedule`, `wordcloud`.
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

## Endpoint Details and Visualizations

### market_data Endpoint
**Data Structure:**
```plaintext
id,name,symbol,price,price_btc,market_cap,percent_change_24h,percent_change_7d,volume_24h,max_supply,circulating_supply,close,galaxy_score,alt_rank,volatility,market_cap_rank
149337,dogwifhat,WIF,2.6033761914520275,3.9433983161915744e-05,2600371121.17,-6.804124838871,17.855925680005,435747308.49,,998845702.63,2.6033761914520275,38,715,0.0366,41
```

**Suggested Visualizations:**
1. **Data Table**: Display the raw data in a tabular format to provide a comprehensive view of all metrics.
2. **Market Cap Indicator**: An indicator showing the current market cap.
3. **Price Indicator with 24h Change**: An indicator showing the current price with the 24-hour change.
4. **24h Volume Indicator with 24h Change**: An indicator showing the 24-hour trading volume with the 24-hour change.
5. **Percentage Changes**: A bar chart showing the percent change over 24 hours and 7 days.

### market_time_series Endpoint
**Data Structure:**
```plaintext
time,open,close,high,low,volume_24h,market_cap,circulating_supply,sentiment,galaxy_score,volatility,alt_rank,contributors_active,contributors_created,posts_active,posts_created,interactions,social_dominance,spam
1721088000,2.171873017532242,2.1605447672,2.2100561258,2.1438554416,589705281.97,2158050911.29,998845728.19,84,49.0,0.0761,126,274,5.0,330,5.0,1831,0.09894933793897524,1
```

**Suggested Visualizations:**

1. **Data Table**: Display the raw data in a tabular format for detailed inspection.
2. **Price Movement Over Time**: A line chart showing the open, close, high, and low prices over time.
3. **Volume and Market Cap Over Time**: A dual-axis line chart with volume on one axis and market cap on the other.
4. **Social Sentiment Over Time**: A line chart showing the sentiment score over time.

### top_creators Endpoint
**Data Structure:**
```plaintext
creator_id,creator_name,creator_display_name,creator_avatar,creator_followers,creator_posts,creator_rank,interactions_24h
twitter::1621096802903818241,MarketCoinpedia,Coinpedia Markets,https://pbs.twimg.com/profile_images/1629009962595926018/3JFmewmb_200x200.jpg,6033,4,1,7722
```

**Suggested Visualizations:**

1. **Data Table**: Display the raw data in a tabular format for detailed inspection.
2. **Bar Chart of Interactions**: A bar chart showing the number of interactions in the last 24 hours for each creator.
3. **Follower Count Distribution**: A bar chart or histogram displaying the distribution of follower counts among the top creators.
4. **Post Activity**: A bar chart comparing the number of posts made by each creator in the last 24 hours.

### top_posts Endpoint
**Data Structure:**
```plaintext
id,post_type,post_title,post_link,post_created,post_sentiment,creator_id,creator_name,creator_display_name,creator_followers,creator_avatar,interactions_24h,interactions_total
1815724005057269901,tweet,The phryge is a hat and a symbol of liberty in Europe. Branding similar to dogwifhat can go extremely viral in the Olympics. Free marketing around the world.,https://twitter.com/phryges_2024X/status/1815724005057269901,1721737311,3.06,twitter::1803386626741248002,phryges_2024X,Olympic 2024 Mascot - $PHRYGES,131,https://pbs.twimg.com/profile_images/1815689298110521344/jgHlx01B_200x200.jpg,1744,

1744
```

**Suggested Visualizations:**

1. **Data Table**: Display the raw data in a tabular format for detailed inspection.
2. **Interactions Over Time**: A line chart showing interactions over time for each post.
3. **Sentiment Distribution**: A bar chart displaying the sentiment scores of the posts.
4. **Top Posts by Interaction**: A bar chart showing the top posts based on the number of interactions.

### topic_summary Endpoint
**Data Structure:**
```plaintext
topic,title,topic_rank,related_topics,types_count,types_interactions,types_sentiment,types_sentiment_detail,interactions_1h,interactions_24h,num_contributors,num_posts,categories,trend
dogwifhat,Dogwifhat,2959,"['$dogwifhat', '$doge', '$mkr', '$cwif', '$byte', '$brett', '$floki', '$pepe', 'bitcoin', 'ethereum', 'memecoin', 'market cap', 'memecoins', 'doge', 'ansem', 'nft', 'cryptocurrencies', 'helium', 'rockstar', 'altcoins']","{'youtube-video': 127, 'tweet': 1058, 'reddit-post': 72, 'tiktok-video': 69}","{'youtube-video': 2958, 'tweet': 49864, 'reddit-post': 199, 'tiktok-video': 39705}","{'youtube-video': 92, 'tweet': 86, 'reddit-post': 90, 'tiktok-video': 62}","{'youtube-video': {'positive': 2559, 'neutral': 390, 'negative': 9}, 'tweet': {'positive': 24893, 'neutral': 23755, 'negative': 1216}, 'reddit-post': {'positive': 105, 'neutral': 94, 'negative': 0}, 'tiktok-video': {'positive': 1414, 'neutral': 37680, 'negative': 611}}",411,92726,283,1326,['Cryptocurrencies'],down
```

**Suggested Visualizations:**

1. **Data Table**: Display the raw data in a tabular format for detailed inspection.
2. **Interactions by Type**: A bar chart showing the number of interactions by type (e.g., YouTube video, tweet, Reddit post, TikTok video).
3. **Sentiment Analysis**: A grouped bar chart displaying positive, neutral, and negative sentiments across different content types.
4. **Trend and Engagement Over Time**: A line chart showing interactions over different time intervals (1 hour, 24 hours).
5. **Related Topics**: A word cloud or a bar chart showing the related topics.

### topic_time_series Endpoint
**Data Structure:**
```plaintext
time,posts_created,posts_active,interactions,contributors_created,contributors_active,sentiment,spam
1721088000,5.0,330,1831,5.0,274,84,
1721091600,1.0,332,1459,1.0,265,81,
```

**Suggested Visualizations:**

1. **Data Table**: Display the raw data in a tabular format for detailed inspection.
2. **Interactions Over Time**: A line chart showing the number of interactions over time.
3. **Sentiment Over Time**: A line chart showing sentiment scores over time.
4. **Post and Contributor Activity**: A grouped bar chart comparing the number of posts created, posts active, contributors created, and contributors active over time.

