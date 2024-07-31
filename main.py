import os
import pandas as pd
from lunar_crush_api.market_data import process_market_data, generate_market_data_charts
from lunar_crush_api.market_time_series import process_market_time_series, generate_market_time_series_charts
from lunar_crush_api.top_creators import process_top_creators, generate_top_creators_charts
from lunar_crush_api.top_posts import process_top_posts, generate_top_posts_charts
from lunar_crush_api.topic_summary import process_topic_summary, generate_topic_summary_charts
from lunar_crush_api.topic_time_series import process_topic_time_series, generate_topic_time_series_charts
from lunar_crush_api.coin_comparison import generate_comparison_charts
from gecko_terminal_api.pools_data import process_pools_data, generate_pools_data_charts

def save_to_csv(df, filename):
    os.makedirs('data', exist_ok=True)
    filepath = os.path.join('data', filename)
    df.to_csv(filepath, index=False)

def generate_index_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Charts Index</title>
    </head>
    <body>
        <h1>Charts Index</h1>
        <ul>
            <li><a href="market_cap_over_time.html">Market Cap Over Time</a></li>
            <li><a href="price_movement_over_time.html">Price Movement Over Time</a></li>
            <li><a href="volume_market_cap_over_time.html">Volume and Market Cap Over Time</a></li>
            <li><a href="market_data.html">Market Data</a></li>
            <li><a href="top_creators.html">Top Creators</a></li>
            <li><a href="top_posts_table.html">Top Posts Table</a></li>
            <li><a href="sentiment_distribution.html">Sentiment Distribution for Top Posts</a></li>
            <li><a href="top_posts_by_interactions.html">Top Posts by Interactions</a></li>
            <li><a href="topic_summary_table.html">Topic Summary Table</a></li>
            <li><a href="related_topics_wordcloud.html">Related Topics Wordcloud</a></li>
            <li><a href="topic_time_series.html">Topic Time Series</a></li>
            <li><a href="pools_data.html">Pools Data</a></li>
            <li><a href="market_cap_comparison.html">Market Cap Comparison</a></li>
            <li><a href="volume_comparison.html">Volume Comparison</a></li>
            <li><a href="social_dominance_comparison.html">Social Dominance Comparison</a></li>
            <li><a href="volatility_comparison.html">Volatility Comparison</a></li>
        </ul>
    </body>
    </html>
    """
    with open(os.path.join('charts', 'index.html'), 'w') as f:
        f.write(html_content)

def main():
    dataframes = {}

    # Process and generate charts for market data
    df_market_data = process_market_data()
    save_to_csv(df_market_data, "market_data.csv")
    generate_market_data_charts(df_market_data)
    dataframes["market_data"] = df_market_data

    # Process and generate charts for market time series
    df_market_time_series = process_market_time_series()
    save_to_csv(df_market_time_series, "market_time_series.csv")
    generate_market_time_series_charts(df_market_time_series)
    dataframes["market_time_series"] = df_market_time_series

    # Process and generate charts for top creators
    df_top_creators = process_top_creators()
    save_to_csv(df_top_creators, "top_creators.csv")
    generate_top_creators_charts(df_top_creators)
    dataframes["top_creators"] = df_top_creators

    # Process and generate charts for top posts
    df_top_posts = process_top_posts()
    save_to_csv(df_top_posts, "top_posts.csv")
    generate_top_posts_charts(df_top_posts)
    dataframes["top_posts"] = df_top_posts

    # Process and generate charts for topic summary
    df_topic_summary = process_topic_summary()
    save_to_csv(df_topic_summary, "topic_summary.csv")
    generate_topic_summary_charts(df_topic_summary)
    dataframes["topic_summary"] = df_topic_summary

    # Process and generate charts for topic time series
    df_topic_time_series = process_topic_time_series()
    save_to_csv(df_topic_time_series, "topic_time_series.csv")
    generate_topic_time_series_charts(df_topic_time_series)
    dataframes["topic_time_series"] = df_topic_time_series

    # Process and generate charts for pools data
    df_pools_data = process_pools_data()
    save_to_csv(df_pools_data, "pools_data.csv")
    generate_pools_data_charts(df_pools_data)
    dataframes["pools_data"] = df_pools_data

    # Generate comparison charts for specified coins
    coins = ["wif", "popcat", "doge", "shib", "pepe", "bonk"]
    generate_comparison_charts(coins)

    # Generate index.html
    generate_index_html()

if __name__ == "__main__":
    main()
