import os
import pandas as pd
from lunar_crush_api.market_data import process_market_data, generate_market_data_charts
from lunar_crush_api.market_time_series import process_market_time_series, generate_market_time_series_charts
from lunar_crush_api.top_creators import process_top_creators, generate_top_creators_charts
from lunar_crush_api.top_posts import process_top_posts, generate_top_posts_charts
from lunar_crush_api.topic_summary import process_topic_summary, generate_topic_summary_charts
from lunar_crush_api.topic_time_series import process_topic_time_series, generate_topic_time_series_charts
# Import other necessary modules similarly...

def save_to_csv(df, filename):
    os.makedirs('data', exist_ok=True)
    filepath = os.path.join('data', filename)
    df.to_csv(filepath, index=False)

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

    # Similarly process and generate charts for other datasets...

if __name__ == "__main__":
    main()
