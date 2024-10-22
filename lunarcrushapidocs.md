API Documentation
To get started with the API make sure you have a subscription and an API key. Browse our endpoints for detailed information on making requests. The base URL for the API is available at https://lunarcrush.com/api4 which by default outputs a github markdown style output of the documentation. This documentation is also available in our simplified JSON output which powers this documentation as well as markdown, and OpenAPI v3.
Endpoints
/public/topics/list/v1
Get a list of trending social topics.
/public/topic/:topic/v1
Get summary information for a social topic. The output is a 24 hour aggregation social activity with metrics comparing the latest 24 hours to the previous 24 hours.
/public/topic/:topic/time-series/v1
Get historical time series data for a social topic
/public/topic/:topic/posts/v1
Get the top posts for a social topic. If start time is provided the result will be the top posts by interactions for the time range. If start is not provided it will be the most recent top posts by interactions from the last 24 hours.
/public/topic/:topic/news/v1
Get the top news posts for a social topic. Top news is determined by the metrics related to the social posts that mention the news posts.
/public/topic/:topic/creators/v1
Get the top creators for a social topic
/public/category/:category/v1
Get summary information for a social topic
/public/category/:category/topics/v1
Get the top topics for a social category
/public/category/:category/time-series/v1
Get historical time series data for a social category
/public/category/:category/posts/v1
Get the top posts for a social topic. If start time is provided the result will be the top posts by interactions for the time range. If start is not provided it will be the most recent top posts by interactions from the last 24 hours.
/public/category/:category/news/v1
Get the top news posts for a category. Top news is determined by the metrics related to the social posts that mention the news posts.
/public/category/:category/creators/v1
Get the top creators for a social category
/public/categories/list/v1
Get a list of trending social categories.
/public/creators/list/v1
Get a list of trending social creators over all of social based on interactions. To get lists of creators by category or topic see the topics and categories endpoints.
/public/creator/:network/:id/v1
Get detail information on a specific creator
/public/creator/:network/:id/time-series/v1
Get time series data on a creator.
/public/creator/:network/:id/posts/v1
Get the top posts for a specific creator.
/public/posts/:post_type/:post_id/v1
Get details of a post
/public/posts/:post_type/:post_id/time-series/v1
Get interactions over time for a post. If a post is older than 365 days the time series will be returned as daily interactions, otherwise it hourly interactions
/public/coins/list/v2
Get a general snapshot of LunarCrush metrics on the entire list of tracked coins. It is designed as a lightweight mechanism for monitoring the universe of available assets, either in aggregate or relative to each other. Metrics include Galaxy Score™, AltRank™, price, volatility, 24h percent change, market cap, social mentions, social interactions, social contributors, social dominance, and categories.
/public/coins/list/v1
Lists all coins and tokens supported by LunarCrush. Includes the "topic" endpoint to use to get social data from this asset as a social topic.
/public/coins/:coin/v1
Get market data on a coin or token. Specify the coin to be queried by providing the numeric ID or the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.
/public/coins/:coin/time-series/v2
Get market time series data on a coin or token. Specify the coin to be queried by providing the numeric ID or the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.
/public/coins/:coin/time-series/v1
Get market time series data on a coin or token. Specify the coin to be queried by providing the numeric ID or the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.
/public/coins/:coin/meta/v1
Get meta information for a cryptocurrency project. This includes information such as the website, social media links, and other information.
/public/stocks/list/v2
Get a general snapshot of LunarCrush metrics on the entire list of tracked stocks. It is designed as a lightweight mechanism for monitoring the universe of available assets, either in aggregate or relative to each other. Metrics include Galaxy Score™, AltRank™, floor price, 24h percent change, market cap, social mentions, social interactions, social contributors, social dominance, and categories.
/public/stocks/list/v1
Lists all stocks supported by LunarCrush. Includes the "topic" endpoint to use to get social data from this asset as a social topic.
/public/stocks/:stock/v1
Get market data on a stock. Specify the coin to be queried by providing the numeric ID or the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.
/public/stocks/:stock/time-series/v2
Get market time series data on a stock. Specify the stock to be queried by providing the numeric ID or the symbol of the stock in the input parameter, which can be found by calling the /stocks/list endpoint.
/public/stocks/:stock/time-series/v1
Get market time series data on a stock. Specify the stock to be queried by providing the numeric ID or the symbol of the stock in the input parameter, which can be found by calling the /stocks/list endpoint.
/public/nfts/list/v2
Get a general snapshot of LunarCrush metrics on the entire list of tracked NFTS. It is designed as a lightweight mechanism for monitoring the universe of available assets, either in aggregate or relative to each other. Metrics include Galaxy Score™, AltRank™, floor price, 24h percent change, market cap, social mentions, social interactions, social contributors, social dominance, and categories.
/public/nfts/list/v1
Lists all nft collections supported by LunarCrush. Includes the "topic" endpoint to use to get social data from this nft collection as a social topic.
/public/nfts/:nft/v1
Get market data on an nft collection. Specify the nft to be queried by providing the numeric ID or the slug of the nft in the input parameter, which can be found by calling the /public/nfts/list endpoint.
/public/nfts/:nft/time-series/v2
Get market time series data on a nft. Specify the nft to be queried by providing the numeric ID or the symbol of the nft in the input parameter, which can be found by calling the /nfts/list endpoint.
/public/nfts/:nft/time-series/v1
Get market time series data on an nft collection. Specify the nft to be queried by providing the numeric ID or slug of the nft collection in the input parameter, which can be found by calling the /public/nfts/list endpoint.
/public/searches/search
Get recently popular social posts matching a single search term or phrase. Optionally configure and test a custom search configuration.
/public/searches/list
List all custom search aggregations.
/public/searches/create
Create a custom search aggregation of topics and search terms. Fine tune the posts that get included or excluded. Search terms and configuration cannot be changed once created. If successful returns the new id/slug and the processed search config. Note that search terms will be adjusted and simplified for optimized search and matching.
/public/searches/:slug/update
Update a custom search aggregation name or priority. Search terms and configuration cannot be changed once created.
/public/searches/:slug/delete
Delete a custom search aggregations.
/public/searches/:slug
See the summary output of a custom search aggregation.
/public/system/changes
Updates to potential changes to historical time series data. Search term changes only impact the most recent 72 hours (hourly) or 3 days (daily) data. "full historical" is a change that may impact the full history of data. Each change provides a description of what is impacted and why.


/public/topics/list/v1
Get a list of trending social topics.
/public/topics/list/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/topics/list/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: [ // 1000 items
    {
      topic: donald trump, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Donald Trump, //The case sensitive title of the topic or category
      topic_rank: 1, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 1, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 1, //The topic rank from 24 hours ago
      num_contributors: 69,347, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 546,697, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 38,382,067, //Number of interactions in the last hour
      interactions_24h: 1,950,728,620, //Number of interactions in the last 24 hours
    },
    {
      topic: united states, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: United States of America, //The case sensitive title of the topic or category
      topic_rank: 2, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 3, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 3, //The topic rank from 24 hours ago
      num_contributors: 46,684, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 240,823, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 21,478,279, //Number of interactions in the last hour
      interactions_24h: 927,995,590, //Number of interactions in the last 24 hours
    },
    {
      topic: kamala harris, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Kamala Harris, //The case sensitive title of the topic or category
      topic_rank: 3, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 7, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 4, //The topic rank from 24 hours ago
      num_contributors: 33,316, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 239,332, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 15,438,081, //Number of interactions in the last hour
      interactions_24h: 578,869,026, //Number of interactions in the last 24 hours
    },
    {
      topic: elon musk, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Elon Musk, //The case sensitive title of the topic or category
      topic_rank: 4, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 5, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 3, //The topic rank from 24 hours ago
      num_contributors: 34,223, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 247,177, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 7,674,167, //Number of interactions in the last hour
      interactions_24h: 1,645,481,716, //Number of interactions in the last 24 hours
    },
    {
      topic: tiktok, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: TikTok, //The case sensitive title of the topic or category
      topic_rank: 5, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 5, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 5, //The topic rank from 24 hours ago
      num_contributors: 28,114, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 131,581, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 8,732,440, //Number of interactions in the last hour
      interactions_24h: 627,966,274, //Number of interactions in the last 24 hours
    },
    {
      topic: youtube, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: YouTube, //The case sensitive title of the topic or category
      topic_rank: 6, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 4, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 7, //The topic rank from 24 hours ago
      num_contributors: 37,067, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 185,195, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 7,109,001, //Number of interactions in the last hour
      interactions_24h: 626,411,855, //Number of interactions in the last 24 hours
    },
    {
      topic: twitter, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: X, //The case sensitive title of the topic or category
      topic_rank: 7, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 8, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 10, //The topic rank from 24 hours ago
      num_contributors: 22,846, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 87,180, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 7,847,943, //Number of interactions in the last hour
      interactions_24h: 191,341,125, //Number of interactions in the last 24 hours
    },
    {
      topic: israel, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Israel, //The case sensitive title of the topic or category
      topic_rank: 8, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 5, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 6, //The topic rank from 24 hours ago
      num_contributors: 21,393, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 161,901, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 4,752,338, //Number of interactions in the last hour
      interactions_24h: 258,718,837, //Number of interactions in the last 24 hours
    },
    {
      topic: india, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: India, //The case sensitive title of the topic or category
      topic_rank: 9, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 8, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 16, //The topic rank from 24 hours ago
      num_contributors: 17,058, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 102,456, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 4,791,272, //Number of interactions in the last hour
      interactions_24h: 314,610,187, //Number of interactions in the last 24 hours
    },
    {
      topic: instagram, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Instagram, //The case sensitive title of the topic or category
      topic_rank: 10, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 12, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 11, //The topic rank from 24 hours ago
      num_contributors: 15,492, //The number of unique social contributors to the topic
      social_dominance:  The percent of the total social volume that this topic represents
      num_posts: 58,466, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 5,034,187, //Number of interactions in the last hour
      interactions_24h: 384,079,500, //Number of interactions in the last 24 hours
    }
      ...990 more
  ]
},


/public/topic/:topic/v1
Get summary information for a social topic. The output is a 24 hour aggregation social activity with metrics comparing the latest 24 hours to the previous 24 hours.
Changes
2024-04-14: More detailed sentiment information has been added to the topic detail outputs
Inputs
Name
Editable-input
Type
Example
Required
topic
bitcoin
string
bitcoin
Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $. You can also look up a topic by the coin/nft/stock numeric id like coins:1 for bitcoin or stocks:7056 for nVidia.
/public/topic/bitcoin/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/topic/bitcoin/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: {
    topic: bitcoin, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
    title: Bitcoin, //The case sensitive title of the topic or category
    topic_rank: 11, //LunarCrush metric for ranking a social topic relative to all other social topics
    related_topics: [ an array of related topics
      crypto,
      eth,
      ethereum,
      solana,
      sol,
      cryptocurrency,
      dogecoin,
      doge,
      bnb,
      blockchain,
        ...90 more
    ],
    types_count: { An object with the counts of the total number of unique posts getting interactions from each social network in the last 24 hours
      news: 365,
      reddit-post: 5,982,
      tiktok-video: 6,723,
      tweet: 187,457,
      youtube-video: 13,961,
    },
    types_interactions: { An object with the counts of the total number of interactions on each post from each social network in the last 24 hours
      news: 47,442,
      reddit-post: 119,381,
      tiktok-video: 5,363,501,
      tweet: 104,642,204,
      youtube-video: 17,436,030,
    },
    types_sentiment: { An object with the sentiment score broken down by each supported social network. 0% is all posts negative, 100% is all posts positive. 50% is equal positive and negative posts. Each post is weighted by interactions.
      news: 75,
      reddit-post: 77,
      tiktok-video: 69,
      tweet: 82,
      youtube-video: 83,
    },
    types_sentiment_detail: { An object with the breakdown of positive, neutral, and negative posts by 24h interactions for each social network
      news: {
        positive: 8,158,
        neutral: 37,914,
        negative: 1,370,
      },
      reddit-post: {
        positive: 26,718,
        neutral: 82,284,
        negative: 10,379,
      },
      tiktok-video: {
        positive: 1,091,097,
        neutral: 3,755,981,
        negative: 516,423,
      },
      tweet: {
        positive: 57,491,805,
        neutral: 38,095,592,
        negative: 9,054,807,
      },
      youtube-video: {
        positive: 11,067,943,
        neutral: 4,746,375,
        negative: 1,621,712,
      }
    },
    interactions_1h: 3,722,716, //Number of interactions in the last hour
    interactions_24h: 127,608,558, //Number of interactions in the last 24 hours
    num_contributors: 23,808, //The number of unique social contributors to the topic
    num_posts: 214,488, //Total number of posts with interactions on this topic in the last 24 hours
    categories: [ an array of categories this topic aggregates into
      Cryptocurrencies,
    ],
    trend: flat, //One of up, down or flat to represent the general trend in interactions
  }
},


/public/topic/:topic/time-series/v1
This endpoint requires the professional plan with upgraded API access.
Get historical time series data for a social topic
Changes
2023-12-30: Introducing new topic time series endpoint to get various hourly or daily time series metrics for a topic.
Inputs
Name
Editable-input
Type
Example
Required
topic
bitcoin
string
bitcoin
Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $.
bucket
hour
string
bucket time series data into hours or days. default is hours.
interval
1w
string
Use interval to specify the start and end time automatically for convenience. If "start" or "end" parameters are provided this parameter is ignored.
start
Select date and time
timestamp
The start time (unix timestamp) to go back to.
end
Select date and time
timestamp
The end time (unix timestamp) to stop at.
/public/topic/bitcoin/time-series/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/topic/bitcoin/time-series/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Visualize
interactions
Oct 15
6am
5am
4am
4am
3am
3am
Oct 22
7,769,324
5,826,993
3,884,662
1,942,331
0
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    topic: bitcoin, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
    metrics: all, //Comma separated list of metrics to include or that are included
    interval: 1w, //Typically used for specifying time intervals like 1w = 1 week, 1m = 1 month etc
    bucket: hour, //Data is generally bucketed into hours or days
    start: 1728950400, // Tue, 15 Oct 2024 00:00:00 GMT Start/from unix timestamp (in seconds)
    end: 1729641600, // Wed, 23 Oct 2024 00:00:00 GMT End/to unix timestamp (in seconds)
    generated: 1729625810, // Tue, 22 Oct 2024 19:36:50 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: [ // 188 items
    {
      time: 1728950400, // Tue, 15 Oct 2024 00:00:00 GMT A unix timestamp (in seconds)
      posts_created: 1,184, //number of unique social posts created
      posts_active: 98,456, //number of unique social posts with interactions
      interactions: 4,147,759, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 826, //number of unique social accounts that created new posts
      contributors_active: 46,718, //number of unique social accounts with posts that have interactions
      sentiment: 79, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 222, //The number of posts created that are considered spam
    },
    {
      time: 1728954000, // Tue, 15 Oct 2024 01:00:00 GMT A unix timestamp (in seconds)
      posts_created: 1,208, //number of unique social posts created
      posts_active: 96,517, //number of unique social posts with interactions
      interactions: 4,183,896, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 852, //number of unique social accounts that created new posts
      contributors_active: 46,220, //number of unique social accounts with posts that have interactions
      sentiment: 79, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 247, //The number of posts created that are considered spam
    },
    {
      time: 1728957600, // Tue, 15 Oct 2024 02:00:00 GMT A unix timestamp (in seconds)
      posts_created: 862, //number of unique social posts created
      posts_active: 97,559, //number of unique social posts with interactions
      interactions: 4,162,939, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 675, //number of unique social accounts that created new posts
      contributors_active: 46,660, //number of unique social accounts with posts that have interactions
      sentiment: 79, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 205, //The number of posts created that are considered spam
    },
    {
      time: 1728961200, // Tue, 15 Oct 2024 03:00:00 GMT A unix timestamp (in seconds)
      posts_created: 908, //number of unique social posts created
      posts_active: 97,992, //number of unique social posts with interactions
      interactions: 4,526,830, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 689, //number of unique social accounts that created new posts
      contributors_active: 47,022, //number of unique social accounts with posts that have interactions
      sentiment: 79, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 238, //The number of posts created that are considered spam
    },
    {
      time: 1728964800, // Tue, 15 Oct 2024 04:00:00 GMT A unix timestamp (in seconds)
      posts_created: 1,200, //number of unique social posts created
      posts_active: 96,951, //number of unique social posts with interactions
      interactions: 4,122,899, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 840, //number of unique social accounts that created new posts
      contributors_active: 46,573, //number of unique social accounts with posts that have interactions
      sentiment: 79, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 335, //The number of posts created that are considered spam
    },
    {
      time: 1728968400, // Tue, 15 Oct 2024 05:00:00 GMT A unix timestamp (in seconds)
      posts_created: 1,047, //number of unique social posts created
      posts_active: 96,674, //number of unique social posts with interactions
      interactions: 4,273,645, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 849, //number of unique social accounts that created new posts
      contributors_active: 46,741, //number of unique social accounts with posts that have interactions
      sentiment: 79, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 205, //The number of posts created that are considered spam
    },
    {
      time: 1728972000, // Tue, 15 Oct 2024 06:00:00 GMT A unix timestamp (in seconds)
      posts_created: 1,095, //number of unique social posts created
      posts_active: 98,747, //number of unique social posts with interactions
      interactions: 4,463,865, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 840, //number of unique social accounts that created new posts
      contributors_active: 48,196, //number of unique social accounts with posts that have interactions
      sentiment: 79, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 256, //The number of posts created that are considered spam
    },
    {
      time: 1728975600, // Tue, 15 Oct 2024 07:00:00 GMT A unix timestamp (in seconds)
      posts_created: 1,437, //number of unique social posts created
      posts_active: 95,245, //number of unique social posts with interactions
      interactions: 4,145,840, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 1,070, //number of unique social accounts that created new posts
      contributors_active: 46,322, //number of unique social accounts with posts that have interactions
      sentiment: 80, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 342, //The number of posts created that are considered spam
    },
    {
      time: 1728979200, // Tue, 15 Oct 2024 08:00:00 GMT A unix timestamp (in seconds)
      posts_created: 1,123, //number of unique social posts created
      posts_active: 93,859, //number of unique social posts with interactions
      interactions: 3,958,799, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 781, //number of unique social accounts that created new posts
      contributors_active: 45,729, //number of unique social accounts with posts that have interactions
      sentiment: 80, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 334, //The number of posts created that are considered spam
    },
    {
      time: 1728982800, // Tue, 15 Oct 2024 09:00:00 GMT A unix timestamp (in seconds)
      posts_created: 1,055, //number of unique social posts created
      posts_active: 87,144, //number of unique social posts with interactions
      interactions: 4,452,866, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      contributors_created: 783, //number of unique social accounts that created new posts
      contributors_active: 42,800, //number of unique social accounts with posts that have interactions
      sentiment: 80, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 271, //The number of posts created that are considered spam
    }
      ...178 more
  ]
},

/public/topic/:topic/posts/v1
Get the top posts for a social topic. If start time is provided the result will be the top posts by interactions for the time range. If start is not provided it will be the most recent top posts by interactions from the last 24 hours.
Changes
2023-11-27: Introducing new topic posts endpoint to get the top social posts for a specific topic.
2024-01-08: Now includes the creator avatar url
2024-02-21: Sentiment is now included in the post object.
2024-02-22: Post output now includes a link to the original post as key "post_link".
2024-02-22: Start and end parameters added so you can fetch the top posts for a specific day or a range of days.
2024-08-29: Added the primary image as post_image to the post object if available.
Inputs
Name
Editable-input
Type
Example
Required
topic
bitcoin
string
bitcoin
Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $.
start
Select date and time
timestamp
The start time (unix timestamp) to start at. Will be rounded to the beginning of the day. If the end parameter is not provided it will just be the top posts for this day.
end
Select date and time
timestamp
(Optional) The end time (unix timestamp) to stop at. Will be rounded to the end of the day.
/public/topic/bitcoin/posts/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/topic/bitcoin/posts/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    topic: bitcoin, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
    type: topic, //Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
    id: bitcoin, //Unique id of the social post
    generated: 1729625826, // Tue, 22 Oct 2024 19:37:06 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: [ // 100 items
    {
      id: 1811250011545686043, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: 🚨New to #Bitcoin? Let us help you get started with a welcome gift!

🎁Limited time only with up to 5,020 $USDT in rewards!

👇Click on Claim Now

#Bybit, //The title text of the social post
      post_link: https://x.com/Bybit_Official/status/1811250011545686043, //The URL to view the social post on the social network
      post_image:  The URL to the primary image for the post if available
      post_created: 1720670628, // Thu, 11 Jul 2024 04:03:48 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.51, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::999947328621395968, //The [network]::[unique_id] for the influencer
      creator_name: Bybit_Official, //The unique screen name for the influencer
      creator_display_name: Bybit, //The chosen display name for the influencer if available
      creator_followers: 4,728,798, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1836056458288566272/Ygr2Wv2k_200x200.png, //The URL to the avatar for the creator
      interactions_24h: 5,834,260, //Number of interactions in the last 24 hours
      interactions_total: 299,404,989, //Number of total interactions
    },
    {
      id: r6UQK41yuzE, //Unique id of the social post
      post_type: youtube-video, //The type of social post
      post_title: Bitcoin ETF Greenlight! 🚀 BlackRock’s Crypto Play & Worldcoin’s Shocking Rebrand! - 🍅 TOMATO NEWS, //The title text of the social post
      post_link: https://youtube.com/watch?v=r6UQK41yuzE, //The URL to view the social post on the social network
      post_image:  The URL to the primary image for the post if available
      post_created: 1729586704, // Tue, 22 Oct 2024 08:45:04 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.31, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: youtube::UCzhLhU-OeaXP4nlaMvJfKUQ, //The [network]::[unique_id] for the influencer
      creator_name: tomarketai, //The unique screen name for the influencer
      creator_display_name: Tomato News by Tomarket, //The chosen display name for the influencer if available
      creator_followers: 2,470,000, //number of followers the account has
      creator_avatar: https://yt3.ggpht.com/HihYtFoCrCMsrf14f4JSeh61U3M2u4QJEgcUGGViHXbNXDySJn46hONFTJbrTaZoyP63X8RarA=s88-c-k-c0x00ffffff-no-rj, //The URL to the avatar for the creator
      interactions_24h: 1,625,502, //Number of interactions in the last 24 hours
      interactions_total: 1,775,285, //Number of total interactions
    },
    {
      id: 1847193651585470820, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: Bitcoin #Whitepaper published 16 years ago was a must-read for all crypto hodlers.

But nowadays how many of us still read whitepaper before crypto trading? 

🫵 We need your feedback! Complete the survey for a chance to win 1,000 USDT. 

#WhyWhitePaper 

Go ⤵️, //The title text of the social post
      post_link: https://x.com/bitgetglobal/status/1847193651585470820, //The URL to view the social post on the social network
      post_image:  The URL to the primary image for the post if available
      post_created: 1729240260, // Fri, 18 Oct 2024 08:31:00 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.34, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::1098881129057112064, //The [network]::[unique_id] for the influencer
      creator_name: bitgetglobal, //The unique screen name for the influencer
      creator_display_name: Bitget, //The chosen display name for the influencer if available
      creator_followers: 4,105,394, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1844611097804013573/hq1F3aqD_200x200.png, //The URL to the avatar for the creator
      interactions_24h: 5,169,745, //Number of interactions in the last 24 hours
      interactions_total: 13,154,288, //Number of total interactions
    },
    {
      id: 1687052892614881280, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: Buy BTC, ETH and 250+ top coins easily with your local currency., //The title text of the social post
      post_link: https://x.com/cryptocom/status/1687052892614881280, //The URL to view the social post on the social network
      post_image:  The URL to the primary image for the post if available
      post_created: 1691059728, // Thu, 03 Aug 2023 10:48:48 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.25, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::864347902029709314, //The [network]::[unique_id] for the influencer
      creator_name: cryptocom, //The unique screen name for the influencer
      creator_display_name: Crypto.com, //The chosen display name for the influencer if available
      creator_followers: 2,838,932, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1823982186430660608/mz_MOBJ6_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 1,864,172, //Number of interactions in the last 24 hours
      interactions_total: 181,342,191, //Number of total interactions
    },
    {
      id: 1805615707180384676, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: We’re thrilled that @nubank has selected @Lightspark to bring the Bitcoin Lightning Network and Universal Money Addresses via the @umastandard to its platform and 100 million customers. We’re working with the Nu team on the technical integration and will have more to share in the future. Read more here: ⚡, //The title text of the social post
      post_link: https://x.com/lightspark/status/1805615707180384676, //The URL to view the social post on the social network
      post_image: https://pbs.twimg.com/media/GQ7RO1xaQAIsxmw.png, //The URL to the primary image for the post if available
      post_created: 1719327305, // Tue, 25 Jun 2024 14:55:05 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.38, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::1518957056522428416, //The [network]::[unique_id] for the influencer
      creator_name: lightspark, //The unique screen name for the influencer
      creator_display_name: Lightspark, //The chosen display name for the influencer if available
      creator_followers: 26,382, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1644476068307570688/JfoIaKt9_200x200.png, //The URL to the avatar for the creator
      interactions_24h: 1,668,723, //Number of interactions in the last 24 hours
      interactions_total: 117,032,375, //Number of total interactions
    },
    {
      id: SPn-weExzOU, //Unique id of the social post
      post_type: youtube-video, //The type of social post
      post_title: Keeping Your Crypto Safe: Best Security Practices | Part 5 of 5 | MemeFi, //The title text of the social post
      post_link: https://youtube.com/watch?v=SPn-weExzOU, //The URL to view the social post on the social network
      post_image:  The URL to the primary image for the post if available
      post_created: 1729620120, // Tue, 22 Oct 2024 18:02:00 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.27, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: youtube::UCY4FcPaaTP04GOVwzoruGhg, //The [network]::[unique_id] for the influencer
      creator_name: memeficlub, //The unique screen name for the influencer
      creator_display_name: MemeFi Club, //The chosen display name for the influencer if available
      creator_followers: 3,840,000, //number of followers the account has
      creator_avatar: https://yt3.ggpht.com/B8cV_CvxdGPaplIJfmE9BVIZ4PKMcPTLynzPDn4z08iVQPEqXsY1A2lsKMxTb2FG4rHzdiWZjQ=s88-c-k-c0x00ffffff-no-rj, //The URL to the avatar for the creator
      interactions_24h: 103,580, //Number of interactions in the last 24 hours
      interactions_total: 103,580, //Number of total interactions
    },
    {
      id: 1848766767142765052, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: The last time a 200+ days consolidation was broken #Bitcoin pumped 172%. 

Bullish🚀, //The title text of the social post
      post_link: https://x.com/rovercrc/status/1848766767142765052, //The URL to view the social post on the social network
      post_image: https://pbs.twimg.com/media/GaePyioXoAAsnQt.jpg, //The URL to the primary image for the post if available
      post_created: 1729615320, // Tue, 22 Oct 2024 16:42:00 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 2.89, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::1353384573435056128, //The [network]::[unique_id] for the influencer
      creator_name: rovercrc, //The unique screen name for the influencer
      creator_display_name: Crypto Rover, //The chosen display name for the influencer if available
      creator_followers: 859,500, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1644208356523909122/M6D7PfWS_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 43,794, //Number of interactions in the last 24 hours
      interactions_total: 66,103, //Number of total interactions
    },
    {
      id: 1848741022987125244, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: I like to imagine a future where the CIA sits on the fact they invented Bitcoin until one BTC is worth $100M, at which point they sell Satoshi’s stash ($110T) to clear out the national debt and cement their place in history as the greatest deep state known to man, //The title text of the social post
      post_link: https://x.com/Nexuist/status/1848741022987125244, //The URL to view the social post on the social network
      post_image:  The URL to the primary image for the post if available
      post_created: 1729609182, // Tue, 22 Oct 2024 14:59:42 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.28, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::1374052664, //The [network]::[unique_id] for the influencer
      creator_name: Nexuist, //The unique screen name for the influencer
      creator_display_name: andi (e/alb), //The chosen display name for the influencer if available
      creator_followers: 13,593, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1774796968327360512/TZ4U-tXm_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 231,904, //Number of interactions in the last 24 hours
      interactions_total: 231,905, //Number of total interactions
    },
    {
      id: 1848450371494334627, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: Absolutely!

- My 401K is up 47%.

- My Bitcoin has skyrocketed by 118%.

- My home value has increased by 80%.

- I no longer worry about COVID.

- My business is bringing in 140% more revenue and 97% more profit.

- Everyone close to me have jobs and healthcare.

- I haven't had to fear for democracy, except for recently.

- And best of all, I no longer need to explain to my kids why the president talks about disturbing things or brags about sexual assault., //The title text of the social post
      post_link: https://x.com/krassenstein/status/1848450371494334627, //The URL to view the social post on the social network
      post_image: https://pbs.twimg.com/media/GacB3g7XwAAPq84.jpg, //The URL to the primary image for the post if available
      post_created: 1729539885, // Mon, 21 Oct 2024 19:44:45 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.13, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::133938408, //The [network]::[unique_id] for the influencer
      creator_name: krassenstein, //The unique screen name for the influencer
      creator_display_name: Brian Krassenstein, //The chosen display name for the influencer if available
      creator_followers: 869,656, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1699761753230299136/zTVYw4j0_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 1,227,198, //Number of interactions in the last 24 hours
      interactions_total: 1,382,286, //Number of total interactions
    },
    {
      id: 1763126977790087276, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: Build your crypto portfolio with just US$10 and start trading over 250 cryptocurrencies, including BTC, ETH, and more., //The title text of the social post
      post_link: https://x.com/cryptocom/status/1763126977790087276, //The URL to view the social post on the social network
      post_image:  The URL to the primary image for the post if available
      post_created: 1709197203, // Thu, 29 Feb 2024 09:00:03 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.17, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::864347902029709314, //The [network]::[unique_id] for the influencer
      creator_name: cryptocom, //The unique screen name for the influencer
      creator_display_name: Crypto.com, //The chosen display name for the influencer if available
      creator_followers: 2,838,932, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1823982186430660608/mz_MOBJ6_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 963,719, //Number of interactions in the last 24 hours
      interactions_total: 13,001,116, //Number of total interactions
    }
      ...90 more
  ]
},

/public/topic/:topic/news/v1
This endpoint is under active development and may still continue to have changes and bug fixes.
Get the top news posts for a social topic. Top news is determined by the metrics related to the social posts that mention the news posts.
Changes
2024-08-29: Introducing new topic news endpoint to get the top news posts for a specific topic.
Inputs
Name
Editable-input
Type
Example
Required
topic
bitcoin
string
bitcoin
Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $.
/public/topic/bitcoin/news/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/topic/bitcoin/news/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    topic: bitcoin, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
    type: topic, //Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
    id: bitcoin, //LunarCrush internal ID for the asset
    generated: 1729625841, // Tue, 22 Oct 2024 19:37:21 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: [ // 99 items
    {
      id: news.bitcoin.com-2587094106, //LunarCrush internal ID for the asset
      post_type: news, //The type of social post
      post_title: Astra Nova: The Tier 1 Web3 Game Booming With 170,000+ Active Users Pre-Token Launch – Press release Bitcoin News, //The title text of the social post
      post_link: https://news.bitcoin.com/astra-nova-the-tier-1-web3-game-booming-with-170000-active-users-pre-token-launch/, //The URL to view the social post on the social network
      post_image: https://static.news.bitcoin.com/wp-content/uploads/2024/07/photo_2024-07-08_15-00-10.jpg, //The URL to the primary image for the post if available
      post_created: 1720439996, // Mon, 08 Jul 2024 11:59:56 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.14, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::3367334171, //The [network]::[unique_id] for the influencer
      creator_name: BTCTN, //The unique screen name for the influencer
      creator_display_name: Bitcoin.com News, //The chosen display name for the influencer if available
      creator_followers: 2,999,407, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1651108008200482816/EJc2IcUa_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 624, //Number of interactions in the last 24 hours
      interactions_total: 210,817, //Number of total interactions
    },
    {
      id: cointelegraph.com-3765870523, //LunarCrush internal ID for the asset
      post_type: news, //The type of social post
      post_title: Here’s what happened in crypto today, //The title text of the social post
      post_link: https://cointelegraph.com/news/what-happened-in-crypto-today, //The URL to view the social post on the social network
      post_image: https://images.cointelegraph.com/cdn-cgi/image/format=auto,onerror=redirect,quality=90,width=1200/https://s3.cointelegraph.com/uploads/2024-08/78d78761-3bd2-4569-96a7-62a97f0a1b0a, //The URL to the primary image for the post if available
      post_created: 1724714669, // Mon, 26 Aug 2024 23:24:29 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::2207129125, //The [network]::[unique_id] for the influencer
      creator_name: Cointelegraph, //The unique screen name for the influencer
      creator_display_name: Cointelegraph, //The chosen display name for the influencer if available
      creator_followers: 2,299,585, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1755983593925378048/kYutau0B_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 893, //Number of interactions in the last 24 hours
      interactions_total: 11,874, //Number of total interactions
    },
    {
      id: decrypt.co-883649776, //LunarCrush internal ID for the asset
      post_type: news, //The type of social post
      post_title: Bitcoin Runes Launch at the Halving: Here’s Everything You Need to Know - Decrypt, //The title text of the social post
      post_link: https://decrypt.co/221962/bitcoin-runes-launch-at-the-halving-heres-everything-you-need-to-know, //The URL to view the social post on the social network
      post_image: https://cdn.decrypt.co/resize/1024/height/512/wp-content/uploads/2024/03/bitcoin-stacks-ai-gID_7.png, //The URL to the primary image for the post if available
      post_created: 1713810070, // Mon, 22 Apr 2024 18:21:10 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.05, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::993530753014054912, //The [network]::[unique_id] for the influencer
      creator_name: decryptmedia, //The unique screen name for the influencer
      creator_display_name: Decrypt, //The chosen display name for the influencer if available
      creator_followers: 197,111, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1814008381453053952/WSQnLfOu_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 632, //Number of interactions in the last 24 hours
      interactions_total: 265,680, //Number of total interactions
    },

/public/topic/:topic/creators/v1
Get the top creators for a social topic
Changes
2023-11-27: Introducing new topic creators endpoint to get the current list of trending social creators for a specific topic
Inputs
Name
Editable-input
Type
Example
Required
topic
bitcoin
string
bitcoin
Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $.
/public/topic/bitcoin/creators/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/topic/bitcoin/creators/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: [ // 1046 items
    {
      creator_id: youtube::UCY4FcPaaTP04GOVwzoruGhg, //The [network]::[unique_id] for the influencer
      creator_name: memeficlub, //The unique screen name for the influencer
      creator_display_name: MemeFi Club, //The chosen display name for the influencer if available
      creator_avatar: https://yt3.ggpht.com/B8cV_CvxdGPaplIJfmE9BVIZ4PKMcPTLynzPDn4z08iVQPEqXsY1A2lsKMxTb2FG4rHzdiWZjQ=s88-c-k-c0x00ffffff-no-rj, //The URL to the avatar for the creator
      creator_followers: 3,840,000, //number of followers the account has
      creator_posts: 32, //total number of posts with interactions in the last 24 hours
      creator_rank: 1, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 6,076,274, //Number of interactions in the last 24 hours
    },
    {
      creator_id: twitter::999947328621395968, //The [network]::[unique_id] for the influencer
      creator_name: Bybit_Official, //The unique screen name for the influencer
      creator_display_name: Bybit, //The chosen display name for the influencer if available
      creator_avatar: https://pbs.twimg.com/profile_images/1836056458288566272/Ygr2Wv2k_200x200.png, //The URL to the avatar for the creator
      creator_followers: 4,728,803, //number of followers the account has
      creator_posts: 4, //total number of posts with interactions in the last 24 hours
      creator_rank: 2, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 5,834,433, //Number of interactions in the last 24 hours
    },
    {
      creator_id: twitter::1098881129057112064, //The [network]::[unique_id] for the influencer
      creator_name: bitgetglobal, //The unique screen name for the influencer
      creator_display_name: Bitget, //The chosen display name for the influencer if available
      creator_avatar: https://pbs.twimg.com/profile_images/1844611097804013573/hq1F3aqD_200x200.png, //The URL to the avatar for the creator
      creator_followers: 4,105,588, //number of followers the account has
      creator_posts: 13, //total number of posts with interactions in the last 24 hours
      creator_rank: 3, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 5,222,413, //Number of interactions in the last 24 hours
    },
    {
      creator_id: twitter::864347902029709314, //The [network]::[unique_id] for the influencer
      creator_name: cryptocom, //The unique screen name for the influencer
      creator_display_name: Crypto.com, //The chosen display name for the influencer if available
      creator_avatar: https://pbs.twimg.com/profile_images/1823982186430660608/mz_MOBJ6_200x200.jpg, //The URL to the avatar for the creator
      creator_followers: 2,838,932, //number of followers the account has
      creator_posts: 30, //total number of posts with interactions in the last 24 hours
      creator_rank: 4, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 4,073,061, //Number of interactions in the last 24 hours
    },
    {
      creator_id: twitter::1353384573435056128, //The [network]::[unique_id] for the influencer
      creator_name: rovercrc, //The unique screen name for the influencer
      creator_display_name: Crypto Rover, //The chosen display name for the influencer if available
      creator_avatar: https://pbs.twimg.com/profile_images/1644208356523909122/M6D7PfWS_200x200.jpg, //The URL to the avatar for the creator
      creator_followers: 859,506, //number of followers the account has
      creator_posts: 423, //total number of posts with interactions in the last 24 hours
      creator_rank: 5, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 2,480,898, //Number of interactions in the last 24 hours
    },
    {
      creator_id: twitter::361289499, //The [network]::[unique_id] for the influencer
      creator_name: BitcoinMagazine, //The unique screen name for the influencer
      creator_display_name: Bitcoin Magazine, //The chosen display name for the influencer if available
      creator_avatar: https://pbs.twimg.com/profile_images/14

/public/category/:category/v1
Get summary information for a social topic
Changes
2023-11-27: Introducing new category detail endpoint to get details for a specific social category.
Inputs
Name
Editable-input
Type
Example
Required
category
musicians
string
musicians
Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces
/public/category/musicians/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/category/musicians/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: {
    topic: musicians, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
    title: Musicians, //The case sensitive title of the topic or category
    category_rank: 6, //LunarCrush metric for ranking a social topic relative to all other social topics
    interactions_1h: 11,029,001, //Number of interactions in the last hour
    interactions_24h: 1,740,005,778, //Number of interactions in the last 24 hours
  }
},

/public/category/:category/topics/v1
Get the top topics for a social category
Changes
2023-11-27: Introducing new category topics endpoint to get the most popular topics within a social category.
Inputs
Name
Editable-input
Type
Example
Required
category
musicians
string
musicians
Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $.
/public/category/musicians/topics/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/category/musicians/topics/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: [ // 129 items
    {
      topic: 3,038, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Aerosmith, //The case sensitive title of the topic or category
      topic_rank: 1,446, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 1,053, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 1,816, //The topic rank from 24 hours ago
      num_contributors: 1,444, //The number of unique social contributors to the topic
      social_dominance: 0.08, //The percent of the total social volume that this topic represents
      num_posts: 1,745, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 14,012, //Number of interactions in the last hour
      interactions_24h: 1,656,626, //Number of interactions in the last 24 hours
    },
    {
      topic: 3,045, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Burna Boy, //The case sensitive title of the topic or category
      topic_rank: 308, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 425, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 448, //The topic rank from 24 hours ago
      num_contributors: 3,763, //The number of unique social contributors to the topic
      social_dominance: 1.915, //The percent of the total social volume that this topic represents
      num_posts: 6,777, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 7,590,372, //Number of interactions in the last hour
      interactions_24h: 39,941,513, //Number of interactions in the last 24 hours
    },
    {
      topic: 3,066, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Cole Swindell, //The case sensitive title of the topic or category
      topic_rank: 3,618, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 3,782, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 3,708, //The topic rank from 24 hours ago
      num_contributors: 126, //The number of unique social contributors to the topic
      social_dominance: 0.00, //The percent of the total social volume that this topic represents
      num_posts: 221, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 504, //Number of interactions in the last hour
      interactions_24h: 67,252, //Number of interactions in the last 24 hours
    },
    {
      topic: 3,080, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Lynyrd Skynyrd, //The case sensitive title of the topic or category
      topic_rank: 1,823, //LunarCrush metric for ranking a social topic relative to all other social topics
      topic_rank_1h_previous: 1,823, //The topic rank from 1 hour ago
      topic_rank_24h_previous: 1,725, //The topic rank from 24 hours ago
      num_contributors: 464, //The number of unique social contributors to the topic
      social_dominance: 0.03, //The percent of the total social volume that this topic represents
      num_posts: 530, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 1,618, //Number of interactions in the last hour
      interactions_24h: 558,059, //Number of interactions in the last 24 hours
    },
    {
      topic: 3,094, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
      title: Rihanna, //The case s

/public/category/:category/time-series/v1
This endpoint requires the professional plan with upgraded API access.
Get historical time series data for a social category
Changes
2023-11-27: Introducing new category time series endpoint to get time series metrics for a social category.
Inputs
Name
Editable-input
Type
Example
Required
category
cryptocurrencies
string
cryptocurrencies
Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces.
bucket
hour
string
bucket time series data into hours or days. default is hours.
interval
1w
string
Use interval to specify the start and end time automatically for convenience. If "start" or "end" parameters are provided this parameter is ignored.
start
Select date and time
timestamp
The start time (unix timestamp) to go back to.
end
Select date and time
timestamp
The end time (unix timestamp) to stop at.
/public/category/cryptocurrencies/time-series/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/category/cryptocurrencies/time-series/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
},

/public/category/:category/posts/v1
This endpoint is under active development and may still continue to have changes and bug fixes.
Get the top posts for a social topic. If start time is provided the result will be the top posts by interactions for the time range. If start is not provided it will be the most recent top posts by interactions from the last 24 hours.
Changes
2024-08-29: Introducing new category news endpoint to get the top news posts for a category.
Inputs
Name
Editable-input
Type
Example
Required
category
cryptocurrencies
string
cryptocurrencies
Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces.
start
Select date and time
timestamp
The start time (unix timestamp) to start at. Will be rounded to the beginning of the day. If the end parameter is not provided it will just be the top posts for this day.
end
Select date and time
timestamp
(Optional) The end time (unix timestamp) to stop at. Will be rounded to the end of the day.
/public/category/cryptocurrencies/posts/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/category/cryptocurrencies/posts/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    category: cryptocurrencies, //LunarCrush social category. Can only includes letters, numbers and spaces
    type: topic, //Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
    id: _cryptocurrencies, //Unique id of the social post
    generated: 1729625893, // Tue, 22 Oct 2024 19:38:13 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: [ // 100 items
    {
      id: 1848775677614370918, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: The most anticipated and hoped-for breakout in history!!  $BTC so, what does that tell you, //The title text of the social post
      post_link: https://x.com/PeterLBrandt/status/1848775677614370918, //The URL to view the social post on the social network
      post_image: https://pbs.twimg.com/media/GagrrZUWYAATOIG.jpg, //The URL to the primary image for the post if available
      post_created: 1729617444, // Tue, 22 Oct 2024 17:17:24 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.1, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::247857712, //The [network]::[unique_id] for the influencer
      creator_name: PeterLBrandt, //The unique screen name for the influencer
      creator_display_name: Peter Brandt, //The chosen display name for the influencer if available
      creator_followers: 743,999, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1818975493909102592/qg-ZI8ES_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 136,002, //Number of interactions in the last 24 hours
      interactions_total: 137,355, //Number of total interactions
    },
    {
      id: 1811250011545686043, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: 🚨New to #Bitcoin? Let us help you get started with a welcome gift!

🎁Limited time only with up to 5,020 $USDT in rewards!

👇Click on Claim Now

#Bybit, //The title text of the social post
      post_link: https://x.com/Bybit_Official/status/1811250011545686043, //The URL to view the social post on the social network
      post_image:  The URL to the primary image for the post if available
      post_created: 1720670628, // Thu, 11 Jul 2024 04:03:48 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.51, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::999947328621395968, //The [network]::[unique_id] for the influencer
      creator_name: Bybit_Official, //The unique screen name for the influencer
      creator_display_name: Bybit, //The chosen display name for the influencer if available
      creator_followers: 4,728,798, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1836056458288566272/Ygr2Wv2k_200x200.png, //The URL to the avatar for the creator
      interactions_24h: 5,834,260, //Number of interactions in the last 24 hours
      interactions_total: 299,404,989, //Number of total interactions
    },
    {
      id: 1848297647452700842, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: 📢 Trade KRC20 memecoins $KASPER & compete for a share of 15,000,000 $KASPER! 🎉 This exclusive event for our CoinEx users ends on Oct 28.

Join here📲:
Learn more about this KRC20 coin
 #KASPER ➡️ @KasperCoin, //The title text of the social post
      post_link: https://x.c

/public/category/:category/news/v1
This endpoint is under active development and may still continue to have changes and bug fixes.
Get the top news posts for a category. Top news is determined by the metrics related to the social posts that mention the news posts.
Changes
2024-08-29: Introducing new category news endpoint to get the top news posts for a category.
Inputs
Name
Editable-input
Type
Example
Required
category
cryptocurrencies
string
cryptocurrencies
Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces.
/public/category/cryptocurrencies/news/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/category/cryptocurrencies/news/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    category: cryptocurrencies, //LunarCrush social category. Can only includes letters, numbers and spaces
    type: topic, //Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
    id: _cryptocurrencies, //LunarCrush internal ID for the asset
    generated: 1729625902, // Tue, 22 Oct 2024 19:38:22 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: [ // 98 items
    {
      id: blog.ethereum.org-4267570507, //LunarCrush internal ID for the asset
      post_type: news, //The type of social post
      post_title: Allocation Update - Q2 2024 | Ethereum Foundation Blog, //The title text of the social post
      post_link: https://blog.ethereum.org/2024/08/30/esp-allocation-q224, //The URL to view the social post on the social network
      post_image: https://storage.googleapis.com/ethereum-hackmd/upload_fd63dc334e72e1c2885cb7969adc1faf.jpg, //The URL to the primary image for the post if available
      post_created: 1725038312, // Fri, 30 Aug 2024 17:18:32 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::2312333412, //The [network]::[unique_id] for the influencer
      creator_name: ethereum, //The unique screen name for the influencer
      creator_display_name: Ethereum Foundation, //The chosen display name for the influencer if available
      creator_followers: 3,474,937, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1627642622645878784/TP1GH9TM_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 2,173, //Number of interactions in the last 24 hours
      interactions_total: 803,428, //Number of total interactions
    },
    {
      id: nature.com-2144797096, //LunarCrush internal ID for the asset
      post_type: news, //The type of social post
      post_title: The FlyWire connectome: neuronal wiring diagram of a complete fly brain, //The title text of the social post
      post_link: https://www.nature.com/immersive/d42859-024-00053-4/index.html, //The URL to view the social post on the social network
      post_image: https://www.nature.com/immersive/d42859-024-00053-4/assets/L8LamKQb8r/nature-flywire-cover-sm-1066x600.png, //The URL to the primary image for the post if available
      post_created: 1727823600, // Tue, 01 Oct 2024 23:00:00 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.32, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::487833518, //The [network]::[unique_id] for the influencer
      creator_name: NaturePortfolio, //The unique screen name for the influencer
      creator_display_name: Nature Portfolio, //The chosen display name for the influencer if available
      creator_followers: 2,237,556, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1393205274887049219/CpCGQiVy_200x200.jpg, //The URL to the avatar for the 

/public/category/:category/creators/v1
Get the top creators for a social category
Changes
2023-11-27: Introducing new category creators endpoint to get the top creators for a social category.
Inputs
Name
Editable-input
Type
Example
Required
category
musicians
string
musicians
Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces.
/public/category/musicians/creators/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/category/musicians/creators/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: [ // 1008 items
    {
      creator_id: twitter::1138458175663988738, //The [network]::[unique_id] for the influencer
      creator_name: PopBase, //The unique screen name for the influencer
      creator_display_name: Pop Base, //The chosen display name for the influencer if available
      creator_avatar: https://pbs.twimg.com/profile_images/1268086791443230737/BRGz4AiW_200x200.jpg, //The URL to the avatar for the creator
      creator_followers: 1669368, //number of followers the account has
      creator_rank: 1, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 45,978,414, //Number of interactions in the last 24 hours
    },
    {
      creator_id: twitter::1800840398656442368, //The [network]::[unique_id] for the influencer
      creator_name: ThePadrepr, //The unique screen name for the influencer
      creator_display_name: 𝐏𝐚𝐝𝐫𝐞 🧸✰, //The chosen display name for the influencer if available
      creator_avatar: https://pbs.twimg.com/profile_images/1804959470302175234/jzg-v1KS_200x200.jpg, //The URL to the avatar for the creator
      creator_followers: 19618, //number of followers the account has
      creator_rank: 2, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 37,627,338, //Number of interactions in the last 24 hours
    },
    {
      creator_id: twitter::1088746878227935232, //The [network]::[unique_id] for the influencer
      creator_name: views09, //The unique screen name for the influencer
      creator_display_name: Nungua Burnaboy, //The chosen display name for the influencer if available
      creator_avatar: https://pbs.twimg.com/profile_images/1821270747857203201/8hf_qZyL_200x200.jpg, //The URL to the avatar for the creator
      creator_followers: 165741, //number of followers the account has
      creator_rank: 3, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 25,526,429, //Number of interactions in the last 24 hours
    },
    {
      creator_id: twitter::166747718, //The [network]::[unique_id] for the influencer
      creator_name: tylerthecreator, //The unique screen name for the influencer
      creator_display_name: T, //The chosen display name for the influencer if available
      creator_avatar: https://pbs.twimg.com/profile_images/1685280787577683968/12_TDGiH_200x200.jpg, //The URL to the avatar for the creator
      creator_followers: 9842028, //number of followers the account has
      creator_rank: 4, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 18,513,956, //Number of interactions in the last 24 hours
    },
    {
      creator_id: twitter::805532293951606785, //The [network]::[unique_id] for the influencer
      creator_name: MattWallace888, //The unique screen name for the influencer
      creator_display_name: Matt Wallace, //The chosen display name for the influencer if available

/public/categories/list/v1
Get a list of trending social categories.
Changes
2023-11-27: Introducing new categories endpoint to get the current list of trending social categories.
/public/categories/list/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/categories/list/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: [ // 34 items
    {
      category: musicians, //LunarCrush social category. Can only includes letters, numbers and spaces
      title: Musicians, //The case sensitive title of the topic or category
      category_rank: 6, //LunarCrush metric for ranking a social topic relative to all other social topics
      category_rank_1h_previous: 5, //The topic rank from 1 hour ago
      category_rank_24h_previous: 6, //The topic rank from 24 hours ago
      num_contributors: 182,084, //The number of unique social contributors to the topic
      social_dominance: 7.709, //The percent of the total social volume that this topic represents
      num_posts: 331,816, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 14,361,972, //Number of interactions in the last hour
      interactions_24h: 1,736,599,384, //Number of interactions in the last 24 hours
    },
    {
      category: finance, //LunarCrush social category. Can only includes letters, numbers and spaces
      title: Finance, //The case sensitive title of the topic or category
      category_rank: 5, //LunarCrush metric for ranking a social topic relative to all other social topics
      category_rank_1h_previous: 10, //The topic rank from 1 hour ago
      category_rank_24h_previous: 5, //The topic rank from 24 hours ago
      num_contributors: 411,119, //The number of unique social contributors to the topic
      social_dominance: 5.494, //The percent of the total social volume that this topic represents
      num_posts: 712,973, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 44,869,236, //Number of interactions in the last hour
      interactions_24h: 1,237,686,592, //Number of interactions in the last 24 hours
    },
    {
      category: premier league, //LunarCrush social category. Can only includes letters, numbers and spaces
      title: Premier League, //The case sensitive title of the topic or category
      category_rank: 15, //LunarCrush metric for ranking a social topic relative to all other social topics
      category_rank_1h_previous: 17, //The topic rank from 1 hour ago
      category_rank_24h_previous: 8, //The topic rank from 24 hours ago
      num_contributors: 33,847, //The number of unique social contributors to the topic
      social_dominance: 0.83, //The percent of the total social volume that this topic represents
      num_posts: 75,630, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 1,521,894, //Number of interactions in the last hour
      interactions_24h: 186,739,879, //Number of interactions in the last 24 hours
    },
    {
      category: pga golfers, //LunarCrush social category. Can only includes letters, numbers and spaces
      title: PGA Golfers, //The case sensitive title of the topic or category
      category_rank: 30, //LunarCrush metric for ranking a social topic relative to all other social topics
      category_rank_1h_previous: 33, //The topic rank from 1 hour ago
      category_rank_24h_previous: 30, //The topic rank from 24 hours ago
      num_contributors: 6,128, //The number of unique social contributors to the topic
      social_dominance: 0.02, //The percent of the total social volume that this topic represents
      num_posts: 15,954, //Total number of posts with interactions on this topic in the last 24 hours
      interactions_1h: 29

/public/creators/list/v1
Get a list of trending social creators over all of social based on interactions. To get lists of creators by category or topic see the topics and categories endpoints.
Changes
2023-11-27: Introducing new creators endpoint to get the current list of trending social creators.
/public/creators/list/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/creators/list/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: [ // 1130 items
    {
      creator_name: elonmusk, //The unique screen name for the influencer
      creator_display_name: Elon Musk, //The chosen display name for the influencer if available
      creator_id: 44196397, //The [network]::[unique_id] for the influencer
      creator_network: twitter, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
      creator_avatar: https://pbs.twimg.com/profile_images/1845482317860450309/OrD0ovmf_200x200.jpg, //The URL to the avatar for the creator
      creator_followers: 202,158,806, //number of followers the account has
      creator_posts: 3,374, //total number of posts with interactions in the last 24 hours
      creator_rank: 1, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 1,107,246,314, //Number of interactions in the last 24 hours
    },
    {
      creator_name: HumansNoContext, //The unique screen name for the influencer
      creator_display_name: NO CONTEXT HUMANS, //The chosen display name for the influencer if available
      creator_id: 855300206086168576, //The [network]::[unique_id] for the influencer
      creator_network: twitter, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
      creator_avatar: https://pbs.twimg.com/profile_images/1833050358479826944/A2qj0e6Z_200x200.jpg, //The URL to the avatar for the creator
      creator_followers: 5,549,321, //number of followers the account has
      creator_posts: 991, //total number of posts with interactions in the last 24 hours
      creator_rank: 2, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 165,078,935, //Number of interactions in the last 24 hours
    },
    {
      creator_name: realDonaldTrump, //The unique screen name for the influencer
      creator_display_name: Donald J. Trump, //The chosen display name for the influencer if available
      creator_id: 25073877, //The [network]::[unique_id] for the influencer
      creator_network: twitter, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
      creator_avatar: https://pbs.twimg.com/profile_images/874276197357596672/kUuht00m_200x200.jpg, //The URL to the avatar for the creator
      creator_followers: 91,849,472, //number of followers the account has
      creator_posts: 611, //total number of posts with interactions in the last 24 hours
      creator_rank: 3, //ranking based on all posts in the last 24 hours that have interactions
      interactions_24h: 165,012,236, //Number of interactions in the last 24 hours
    },
    {
      creator_name: PopBase, //The unique screen name for the influencer
      creator_display_name: Pop Base, //The chosen display name for the influencer if available
      creator_id: 1138458175663988738, //The [network]::[unique_id] for the influencer
      creator_network: twitter, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
      creator_avatar: https://pbs.twimg.com/profile_images/1268

/public/creator/:network/:id/v1
Get detail information on a specific creator
Changes
2023-11-27: Introducing new creator detail endpoint to get details for a specific creator.
Inputs
Name
Editable-input
Type
Example
Required
network
twitter
string
twitter
Provide the network for the creator. One of twitter, youtube, instagram, reddit, or tiktok
id
elonmusk
string
elonmusk
Provide the unique ID or screen name of the creator
/public/creator/twitter/elonmusk/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/creator/twitter/elonmusk/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: {
    creator_id: twitter::44196397, //The [network]::[unique_id] for the influencer
    creator_name: elonmusk, //The unique screen name for the influencer
    creator_display_name: Elon Musk, //The chosen display name for the influencer if available
    creator_avatar: https://pbs.twimg.com/profile_images/1845482317860450309/OrD0ovmf_200x200.jpg, //The URL to the avatar for the creator
    creator_followers: 202,160,042, //number of followers the account has
    creator_rank: 1, //ranking based on all posts in the last 24 hours that have interactions
    interactions_24h: 1,113,935,217, //Number of interactions in the last 24 hours
    topic_influence: [ an array of social topics and the creators ranking on each topic
      {
        topic: elon musk, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
        count: 107,
        percent: 10.7,
        rank: 1,
      },
      {
        topic: spacex, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
        count: 41,
        percent: 4.1,
        rank: 1,
      },
      {
        topic: starlink, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
        count: 32,
        percent: 3.2,
        rank: 1,
      },
      {
        topic: future, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
        count: 30,
        percent: 3,
        rank: 1,
      },
      {
        topic: donald trump, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
        count: 25,
        percent: 2.5,
        rank: 2,
      },
      {
        topic: political, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
        count: 22,
        percent: 2

/public/creator/:network/:id/time-series/v1
Get time series data on a creator.
Changes
2024-03-19: Introducing new creator time series endpoint.
Inputs
Name
Editable-input
Type
Example
Required
network
twitter
string
twitter
Influencer social network
id
lunarcrush
string
lunarcrush
The unique id or screen name of the creator
bucket
hour
string
bucket time series data into hours or days. default is hours.
interval
1w
string
Use interval to specify the start and end time automatically for convenience. If "start" or "end" parameters are provided this parameter is ignored.
start
Select date and time
timestamp
The start time (unix timestamp) to go back to.
end
Select date and time
timestamp
The end time (unix timestamp) to stop at.
/public/creator/twitter/lunarcrush/time-series/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/creator/twitter/lunarcrush/time-series/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Visualize
interactions
Oct 15
5am
4am
3am
2am
1am
12am
11pm
Oct 22
91,526
68,644.5
45,763
22,881.5
0
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    network: twitter, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
    metrics: all, //Comma separated list of metrics to include or that are included
    influencer_id: 988992203568562176,
    interval: 1w, //Typically used for specifying time intervals like 1w = 1 week, 1m = 1 month etc
    bucket: hour, //Data is generally bucketed into hours or days
    start: 1728950400, // Tue, 15 Oct 2024 00:00:00 GMT Start/from unix timestamp (in seconds)
    end: 1729641600, // Wed, 23 Oct 2024 00:00:00 GMT End/to unix timestamp (in seconds)
    generated: 1729625953, // Tue, 22 Oct 2024 19:39:13 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: [ // 188 items
    {
      time: 1728950400, // Tue, 15 Oct 2024 00:00:00 GMT A unix timestamp (in seconds)
      posts_created: 69, //number of unique social posts created
      posts_active: 363, //number of unique social posts with interactions
      interactions: 5,656, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      followers: 312,154, //The number of publicly displayed followers the creator has
    },
    {
      time: 1728954000, // Tue, 15 Oct 2024 01:00:00 GMT A unix timestamp (in seconds)
      posts_created: 51, //number of unique social posts created
      posts_active: 363, //number of unique social posts with interactions
      interactions: 4,958, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      followers: 312,152, //The number of publicly displayed followers the creator has
    },
    {
      time: 1728957600, // Tue, 15 Oct 2024 02:00:00 GMT A unix timestamp (in seconds)
      posts_created: 1, //number of unique social posts created
      posts_active: 350, //number of unique social posts with interactions
      interactions: 5,143, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      followers: 312,166, //The number of publicly displayed followers the creator has
    },
    {
      time: 1728961200, // Tue, 15 Oct 2024 03:00:00 GMT A unix timestamp (in seconds)
      posts_created: 44, //number of unique social posts created
      posts_active: 451, //number of unique social posts with interactions
      interactions: 5,151, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      followers: 312,165, //The number of publicly displayed followers the creator has
    },
    {
      time: 1728964800, // Tue, 15 Oct 2024 04:00:00 GMT A unix timestamp (in seconds)
      posts_active: 324, //number of unique social posts with interactions
      interactions: 5,687, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      followers: 312,163, //The number of publicly displayed followers the creator has
    },
    {
      time: 1728968400, // Tue, 15 Oct 2024 05:00:00 GMT A unix timestamp (in seconds)
      posts_active: 320, //number of unique social posts with interactions
      interactions: 6,658, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      followers: 312,189, //The number of publicly displayed followers the creator has
    },
    {
      time: 1728972000, // Tue, 15 Oct 2024 06:00:00 GMT A unix timestamp (in seconds)
      posts_active: 310, //number of unique social posts with interactions
      interactions: 7,311, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      followers: 312,191, //The number of publicly displayed followers the creator has
    },
    {
      time: 1728975600, // Tue, 15 Oct 2024 07:00:00 GMT A unix timestamp (in seconds)
      posts_crea

/public/creator/:network/:id/posts/v1
Get the top posts for a specific creator.
Changes
2024-02-21: Introducing new creator posts endpoint to get the top social posts and details for a specific creator.
2024-02-21: Sentiment is now included in the post object.
2024-02-22: Post output now includes a link to the original post as key "post_link".
2024-03-02: Start and end parameters added so you can fetch the top posts for a specific day or a range of days.
Inputs
Name
Editable-input
Type
Example
Required
network
twitter
string
twitter
Network for the creator. One of twitter, youtube, instagram, reddit, or tiktok
id
elonmusk
string
elonmusk
Unique ID or screen name of the creator
start
Select date and time
timestamp
The start time (unix timestamp) to start at. Will be rounded to the beginning of the day. If the end parameter is not provided it will just be the top posts for this day.
end
Select date and time
timestamp
(Optional) The end time (unix timestamp) to stop at. Will be rounded to the end of the day.
/public/creator/twitter/elonmusk/posts/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/creator/twitter/elonmusk/posts/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: [ // 1000 items
    {
      id: 1848463905778987124, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: Trump 💯 plays for @Steelers 😂, //The title text of the social post
      post_created: 1729543112, // Mon, 21 Oct 2024 20:38:32 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.46, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::44196397, //The [network]::[unique_id] for the influencer
      creator_name: elonmusk, //The unique screen name for the influencer
      creator_display_name: Elon Musk, //The chosen display name for the influencer if available
      creator_followers: 202,160,029, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1845482317860450309/OrD0ovmf_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 59,408,887, //Number of interactions in the last 24 hours
      interactions_total: 64,878,897, //Number of total interactions
    },
    {
      id: 1848375429008073034, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: Take the red pill, //The title text of the social post
      post_created: 1729522018, // Mon, 21 Oct 2024 14:46:58 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::44196397, //The [network]::[unique_id] for the influencer
      creator_name: elonmusk, //The unique screen name for the influencer
      creator_display_name: Elon Musk, //The chosen display name for the influencer if available
      creator_followers: 202,160,129, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1845482317860450309/OrD0ovmf_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 58,915,303, //Number of interactions in the last 24 hours
      interactions_total: 62,688,928, //Number of total interactions
    },
    {
      id: 1848479124190597198, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: Those are the correct lyrics, //The title text of the social post
      post_created: 1729546740, // Mon, 21 Oct 2024 21:39:00 GMT The unix timestamp of our best indication of when the post was created
      post_sentiment: 3.21, //The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
      creator_id: twitter::44196397, //The [network]::[unique_id] for the influencer
      creator_name: elonmusk, //The unique screen name for the influencer
      creator_display_name: Elon Musk, //The chosen display name for the influencer if available
      creator_followers: 202,159,639, //number of followers the account has
      creator_avatar: https://pbs.twimg.com/profile_images/1845482317860450309/OrD0ovmf_200x200.jpg, //The URL to the avatar for the creator
      interactions_24h: 56,584,526, //Number of interactions in the last 24 hours
      interactions_total: 56,223,624, //Number of total interactions
    },
    {
      id: 1848138218673258875, //Unique id of the social post
      post_type: tweet, //The type of social post
      post_title: This is awesome 😎 
, //The title text of the social post
      post_created: 1729465462, // Sun, 20 Oct 2024 23:04:22 GMT The unix timestamp of our best indication of when th

/public/posts/:post_type/:post_id/v1
Get details of a post
Changes
2024-02-10: Introducing the post detail endpoint to get details of a single post
Inputs
Name
Editable-input
Type
Example
Required
post_type
tweet
string
tweet
The post type e.g. tweet, youtube-video, tiktok-video, reddit-post, instagram-post
post_id
1756378079893782591
string
1756378079893782591
The unique id of a post, for twitter it is a number, youtube it is the id in the url after watch?v=, look in the url for the unique id
/public/posts/tweet/1756378079893782591/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/posts/tweet/1756378079893782591/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())


/public/coins/list/v2
This endpoint requires the professional plan with upgraded API access.
Get a general snapshot of LunarCrush metrics on the entire list of tracked coins. It is designed as a lightweight mechanism for monitoring the universe of available assets, either in aggregate or relative to each other. Metrics include Galaxy Score™, AltRank™, price, volatility, 24h percent change, market cap, social mentions, social interactions, social contributors, social dominance, and categories.
Changes
2024-01-03: v2 includes market and social data with options to sort and limit by metrics
2024-01-26: Logos now available for each entry
2024-03-18: Blockchain and contract address info for assets to help clearly identify the asset on chain
2024-04-14: Includes the topic to use when looking up social data for this nft collection as a social topic
2024-09-13: Includes sentiment data
Inputs
Name
Editable-input
Type
Default
Options
sort
market_cap_rank
string
market_cap_rank
id, symbol, name, price, price_btc, volume_24h, volatility, circulating_supply, max_supply, percent_change_1h, percent_change_24h, percent_change_7d, market_cap, market_cap_rank, interactions_24h, social_volume_24h, social_dominance, market_dominance, galaxy_score, galaxy_score_previous, alt_rank, alt_rank_previous, sentiment, blockchain
sort the output by metric
limit
10
number
10
limit the number of results. Default is 10 maximum is 100 per page.
desc
boolean
Pass any value as desc and the output will be reversed (descending)
page
0
0
When using limit, set the page of results to display, pages start at 0
/public/coins/list/v2

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/coins/list/v2', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    limit: 0,
    sort: market_cap_rank,
    desc: true,
    page: 0,
    total_rows: 4,207,
    generated: 1729625991, // Tue, 22 Oct 2024 19:39:51 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: [ // 4207 items
    {
      id: 1, //LunarCrush internal ID for the asset
      symbol: BTC, //The symbol for the asset
      name: Bitcoin, //The full name of the asset
      price: 67,478.848, //Current price in USD
      price_btc: 1, //Current price in BTC
      volume_24h: 32,803,634,029.55, //Volume in USD for 24 hours up to this data point
      volatility: 0.01, //Volatility is calculated as the standard deviation of the price.
      circulating_supply: 19,771,496, //Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
      max_supply: 21,000,000, //The maximum supply of the asset if available
      percent_change_1h: 0.13, //Percent change in price since 1 hour ago
      percent_change_24h: -0.04, //Percent change in price since 24 hours ago
      percent_change_7d: 1.135, //Percent change in price since 7 days ago
      market_cap: 1,334,157,772,435.12, //Total dollar market value of all circulating supply or outstanding shares
      market_cap_rank: 1, //The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
      interactions_24h: 127,035,260, //Number of interactions in the last 24 hours
      social_volume_24h: 214,170, //Total number of posts with interactions on this topic in the last 24 hours
      social_dominance: 23.971, //The percent of the total social volume that this topic represents
      market_dominance: 57.479, //The percent of the total market cap that this asset represents
      market_dominance_prev: 57.276,
      galaxy_score: 69, //A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
        ...11 more
    },
    {
      id: 2, //LunarCrush internal ID for the asset
      symbol: ETH, //The symbol for the asset
      name: Ethereum, //The full name of the asset
      price: 2,627.318, //Current price in USD
      price_btc: 0.04, //Current price in BTC
      volume_24h: 15,720,766,766.64, //Volume in USD for 24 hours up to this data point
      volatility: 0.02, //Volatility is calculated as the standard deviation of the price.
      circulating_supply: 120,392,960.03, //Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
      max_supply:  The maximum supply of the asset if available
      percent_change_1h: 0.02, //Percent change in price since 1 hour ago
      percent_change_24h: -1.755, //Percent change in price since 24 hours ago
      percent_change_7d: 1.616, //Percent change in price since 7 days ago
      market_cap: 316,310,568,658.47, //Total dollar market value of all circulating supply or outstanding shares
      market_cap_rank: 2, //The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
      interactions_24h: 27,472,634, //Number of interactions in the last 24 hours
      social_volume_24h: 78,935, //Total number of posts with interactions on this topic in the last 24 hours
      social_dominance: 8.835, //The percent of the total social volume that this topic represents
      market_dominance: 13.631, //The percent of the total market cap that this asset represents
      market_dominance_prev: 13.583,
      galaxy_score: 65, //A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
        ...11 more
    },
    {
      id: 7, //LunarCrush internal ID for the asset
      symbol: USDT, //The symbol for the asset
      name: Tether, //The full name of the asset
      price: 1.00, //Current price in USD
      price_btc: 0.00, //Current price in BTC
      volume_24h: 59,947,812,223.46, //Volume in USD for 24 hours up to this data point
      volatility: 0.00, //Volatility is calculated as the standard deviation of the price.
      circulating_supply: 120,219,543,500.34, //Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
      max_supply:  The maximum supply of the asset if available
      percent_change_1h: -0.02, //Percent change in price since 1 hour ago
      percent_change_24h: -0.00, //Percent change in price since 24 hours ago
      percent_change_7d: -0.03, //Percent change in price since 7 days ago
      market_cap: 120,158,813,806.38, //Total dollar market value of all circulating supply or outstanding shares
      market_cap_rank: 3, //The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
      interactions_24h: 19,420,045, //Number of interactions in the last 24 hours
      social_volume_24h: 11,490, //Total number of posts with interactions on this topic in the last 24 hours
      social_dominance: 1.286, //The percent of the total social volume that this topic represents
      market_dominance: 5.173, //The percent of the total market cap that this asset represents
      market_dominance_prev: 5.155,
      galaxy_score: 42, //A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
        ...11 more
    },
    {
      id: 6, //LunarCrush internal ID for the asset
      symbol: BNB, //The symbol for the asset
      name: Binance Coin, //The full name of the asset
      price: 594.456, //Current price in USD
      price_btc: 0.01, //Current price in BTC

/public/coins/list/v1
Lists all coins and tokens supported by LunarCrush. Includes the "topic" endpoint to use to get social data from this asset as a social topic.
Changes
2023-11-25: Includes the topic to use when looking up social data for this asset as a social topic
/public/coins/list/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/coins/list/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    sort: market_cap_rank,
    desc: true,
    limit: 0,
    page: 0,
    total_rows: 4,207,
    generated: 1729626211, // Tue, 22 Oct 2024 19:43:31 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: [ // 4207 items
    {
      id: 1, //LunarCrush internal ID for the asset
      symbol: BTC, //The symbol for the asset
      name: Bitcoin, //The full name of the asset
      price: 67,422.147, //Current price in USD
      price_btc: 1, //Current price in BTC
      volume_24h: 32,815,971,053.87, //Volume in USD for 24 hours up to this data point
      volatility: 0.01, //Volatility is calculated as the standard deviation of the price.
      circulating_supply: 19,771,496, //Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
      max_supply: 21,000,000, //The maximum supply of the asset if available
      percent_change_1h: 0.08, //Percent change in price since 1 hour ago
      percent_change_24h: -0.17, //Percent change in price since 24 hours ago
      percent_change_7d: 0.99, //Percent change in price since 7 days ago
      market_cap: 1,333,036,715,971.98, //Total dollar market value of all circulating supply or outstanding shares
      market_cap_rank: 1, //The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
      interactions_24h: 127,035,260, //Number of interactions in the last 24 hours
      social_volume_24h: 214,170, //Total number of posts with interactions on this topic in the last 24 hours
      social_dominance: 23.971, //The percent of the total social volume that this topic represents
      market_dominance: 57.479, //The percent of the total market cap that this asset represents
      market_dominance_prev: 57.276,
      galaxy_score: 69, //A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
        ...11 more
    },
    {
      id: 2, //LunarCrush internal ID for the asset
      symbol: ETH, //The symbol for the asset
      name: Ethereum, //The full name of the asset
      price: 2,625.724, //Current price in USD
      price_btc: 0.04, //Current price in BTC
      volume_24h: 15,706,827,566.08, //Volume in USD for 24 hours up to this data point
      volatility: 0.02, //Volatility is calculated as the standard deviation of the price.
      circulating_supply: 120,392,960.03, //Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
      max_supply:  The maximum supply of the asset if available
      percent_change_1h: 0.02, //Percent change in price since 1 hour ago
      percent_change_24h: -1.872, //Percent change in price since 24 hours ago
      percent_change_7d: 1.539, //Percent change in price since 7 days ago
      market_cap: 316,118,688,804.9, //Total dollar market value of all circulating supply or outstanding shares
      market_cap_rank: 2, //The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
      interactions_24h: 27,472,634, //Number of interactions in the last 24 hours
      social_volume_24h: 78,935, //Total number of posts with interactions on this topic in the last 24 hours
      social_dominance: 8.835, //The percent of the total social volume that this topic represents
      market_dominance: 13.631, //The percent of the total market cap that this asset represents
      market_dominance_prev: 13.583,
      galaxy_score: 65, //A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
        ...11 more
    },
    {

/public/coins/:coin/v1
Get market data on a coin or token. Specify the coin to be queried by providing the numeric ID or the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.
Changes
2023-11-25: The coins endpoint provides the current market data for a crypto asset. Social data has been removed and is available using other endpoints
Inputs
Name
Editable-input
Type
Example
Required
coin
2
string
2
provide the numeric id or symbol of the coin or token.
/public/coins/2/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/coins/2/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    coin: 2,
    generated: 1729626225, // Tue, 22 Oct 2024 19:43:45 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: {
    id: 2, //LunarCrush internal ID for the asset
    name: Ethereum, //The full name of the asset
    symbol: ETH, //The symbol for the asset
    price: 2,626.93, //Current price in USD
    price_btc: 0.04, //Current price in BTC
    market_cap: 316,263,933,933.69, //Total dollar market value of all circulating supply or outstanding shares
    percent_change_24h: -1.679, //Percent change in price since 24 hours ago
    percent_change_7d: 1.463, //Percent change in price since 7 days ago
    percent_change_30d: 2.058, //Percent change in price since 30 days ago
    volume_24h: 15,695,876,401.74, //Volume in USD for 24 hours up to this data point
    max_supply:  The maximum supply of the asset if available
    circulating_supply: 120,392,960.03, //Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
    close: 2,626.93, //Close price for the time period
    galaxy_score: 65, //A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
    alt_rank: 408, //A proprietary score based on how an asset is performing relative to all other assets supported
    volatility: 0.02, //Volatility is calculated as the standard deviation of the price.
    market_cap_rank: 2, //The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
  }
},

/public/coins/:coin/time-series/v2
Get market time series data on a coin or token. Specify the coin to be queried by providing the numeric ID or the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.
Changes
2024-01-04: Introducing new coin time series endpoint v2 that includes market and social data combined.
Inputs
Name
Editable-input
Type
Example
Required
coin
2
string
2
provide the numeric id or symbol of the coin or token.
bucket
hour
string
bucket time series data into hours or days. default is hours.
interval
1w
string
Use interval to specify the start and end time automatically for convenience. If "start" or "end" parameters are provided this parameter is ignored.
start
Select date and time
timestamp
The start time (unix timestamp) to go back to.
end
Select date and time
timestamp
The end time (unix timestamp) to stop at.
/public/coins/2/time-series/v2

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/coins/2/time-series/v2', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Visualize
interactions
Oct 15
7am
7am
8am
8am
8am
9am
Oct 22
2,376,703
1,782,527.25
1,188,351.5
594,175.75
0
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  config: { API request as recognized and processed by LunarCrush
    coin: 2,
    topic: ethereum, //LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
    metrics: all, //Comma separated list of metrics to include or that are included
    interval: 1w, //Typically used for specifying time intervals like 1w = 1 week, 1m = 1 month etc
    bucket: hour, //Data is generally bucketed into hours or days
    start: 1728950400, // Tue, 15 Oct 2024 00:00:00 GMT Start/from unix timestamp (in seconds)
    end: 1729623648, // Tue, 22 Oct 2024 19:00:48 GMT End/to unix timestamp (in seconds)
    generated: 1729626404, // Tue, 22 Oct 2024 19:46:44 GMT A unix timestamp (in seconds) when the data was generated to understand possibly stale data
  },
  data: [ // 188 items
    {
      time: 1728950400, // Tue, 15 Oct 2024 00:00:00 GMT A unix timestamp (in seconds)
      open: 2,622.12, //Open price for the time period
      close: 2,622.121, //Close price for the time period
      high: 2,622.12, //Higest price fo rthe time period
      low: 2,617.615, //Lowest price for the time period
      volume_24h: 21,666,154,539.45, //Volume in USD for 24 hours up to this data point
      market_cap: 315,665,153,770.55, //Total dollar market value of all circulating supply or outstanding shares
      market_dominance: 13.74, //The percent of the total market cap that this asset represents
      circulating_supply: 120,385,428.26, //Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
      sentiment: 85, //% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
      spam: 122, //The number of posts created that are considered spam
      galaxy_score: 70, //A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
      volatility: 0.03, //Volatility is calculated as the standard deviation of the price.
      alt_rank: 104, //A proprietary score based on how an asset is performing relative to all other assets supported
      contributors_active: 18,695, //number of unique social accounts with posts that have interactions
      contributors_created: 229, //number of unique social accounts that created new posts
      posts_active: 33,738, //number of unique social posts with interactions
      posts_created: 353, //number of unique social posts created
      interactions: 797,156, //number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
      social_dominance: 6.103, //The percent of the total social volume that this topic represents
    },
    {
      time: 1728954000, // Tue, 15 Oct 2024 01:00:00 GMT A unix timestamp (in seconds)
      open: 2,622.088, //Open price for the time period
      clos

/public/coins/:coin/meta/v1
Get meta information for a cryptocurrency project. This includes information such as the website, social media links, and other information.
Changes
2024-04-01: New meta information endpoint for coins to get more detailed information about a cryptocurrency.
Inputs
Name
Editable-input
Type
Example
Required
coin
2
string
2
provide the numeric id or symbol of the coin or token.
/public/coins/2/meta/v1

Request
Request
JavaScript fetch
Node.js Axios
Vanilla Node.js
curl
Python Requests
Go
Rust

const response = await fetch('https://lunarcrush.com/api4/public/coins/2/meta/v1', {
    headers: {
        'Authorization': 'Bearer 58hkoe1j90q0shqu655g1b4gjlyymjfrwz5nxafb'
    }
}).then(res => res.json())
Response
Annotated
Formatted JSON
Raw
BigQuery Schema
{
  data: {
    id: 2, //LunarCrush internal ID for the asset
    name: Ethereum, //The full name of the asset
    symbol: ETH, //The symbol for the asset
    market_categories: layer-1,
    updated: 1726082575, // Wed, 11 Sep 2024 19:22:55 GMT Timestamp of when the data was last updated
    blockchain: [ // 7 items
      {
        network: ethereum, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
        address: 0,
        decimals: 18,
      },
      {
        network: bnbchain, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
        address: 0x2170ed0880ac9a755fd29b2688956bd959f933f8,
        decimals: 18,
      },
      {
        network: avalanche, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
        address: 0xf20d962a6c8f70c731bd838a3a388d7d48fa6e15,
        decimals: 18,
      },
      {
        network: arbitrum, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
        address: 0,
        decimals: 18,
      },
      {
        network: optimism, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
        address: 0,
        decimals: 18,
      },
      {
        network: tezos, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
        address: kt19at7rquvyjxnz2fbv7d9zc8rkyg7gaou8,
        decimals: 18,
      },
      {
        network: solana, //The social network for the post or influencer. We still refer to x as twitter out of developer preference.
        address: 2fpytwczlug1mdrwsyop4d6s1tm7hakhyrjknb5w6pxk,
        decimals: 18,
      }
    ],
    short_summary: Ethereum is open access to digital money and data-friendly services for everyone – no matter your background or location. It's a community-built technology behind the cryptocurrency ether (ETH) and thousands of applications you can use toda

