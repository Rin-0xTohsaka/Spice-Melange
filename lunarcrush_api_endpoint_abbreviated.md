# LunarCrush API Documentation

## Overview
The LunarCrush API provides access to social analytics and market data for cryptocurrencies, NFTs, and stocks. This documentation outlines the available endpoints, their parameters, and response formats.

## Base URL
```
https://lunarcrush.com/api4
```

## Authentication
All requests require an API key passed in the Authorization header:
```
Authorization: Bearer YOUR_API_KEY
```

## Response Format
All responses are returned in JSON format and generally follow this structure:
```json
{
  "config": {
    // Request configuration and metadata
    "generated": 1729625810  // Unix timestamp when data was generated
  },
  "data": {
    // Response data
  }
}
```

## Endpoints

### Topics

#### 1. List Topics
```
GET /public/topics/list/v1
```
Returns a list of trending social topics with their metrics.

**Response Fields:**
- `topic`: Topic identifier (letters, numbers, spaces, #, and $ only)
- `title`: Case-sensitive title
- `topic_rank`: Current ranking
- `num_contributors`: Number of unique social contributors
- `num_posts`: Total posts with interactions in last 24h
- `interactions_1h`: Interactions in last hour
- `interactions_24h`: Interactions in last 24 hours

#### 2. Get Topic Details
```
GET /public/topic/:topic/v1
```
Get summary information for a specific social topic.

**Parameters:**
- `topic` (required): Topic identifier (e.g., "bitcoin")

**Response Fields:**
- `topic`: Topic identifier
- `title`: Topic title
- `topic_rank`: Current ranking
- `related_topics`: Array of related topics
- `types_count`: Post counts by platform
- `types_interactions`: Interaction counts by platform
- `types_sentiment`: Sentiment scores by platform

#### 3. Topic Time Series
```
GET /public/topic/:topic/time-series/v1
```
Get historical time series data for a topic.

**Parameters:**
- `topic` (required): Topic identifier
- `bucket`: Data grouping ('hour' or 'day')
- `interval`: Time interval (e.g., "1w" for 1 week)
- `start`: Start timestamp
- `end`: End timestamp

### Categories

#### 1. List Categories
```
GET /public/categories/list/v1
```
Returns a list of trending social categories.

**Response Fields:**
- `category`: Category identifier
- `title`: Category title
- `category_rank`: Current ranking
- `num_contributors`: Unique contributors
- `interactions_24h`: 24-hour interactions

#### 2. Category Details
```
GET /public/category/:category/v1
```
Get summary information for a specific category.

**Parameters:**
- `category` (required): Category identifier (lowercase, letters and numbers only)

### Coins

#### 1. List Coins
```
GET /public/coins/list/v2
```
Get a snapshot of all tracked cryptocurrencies.

**Parameters:**
- `sort`: Sort field (e.g., "market_cap_rank", "price", "volume_24h")
- `limit`: Number of results (default: 10, max: 100)
- `desc`: Boolean for descending order
- `page`: Page number (starts at 0)

**Response Fields:**
- `id`: LunarCrush internal ID
- `symbol`: Asset symbol
- `name`: Full name
- `price`: Current USD price
- `market_cap`: Total market capitalization
- `galaxy_score`: Proprietary technical/social score
- `social_dominance`: Percentage of total social volume

#### 2. Coin Details
```
GET /public/coins/:coin/v1
```
Get detailed market data for a specific coin.

**Parameters:**
- `coin` (required): Coin ID or symbol

#### 3. Coin Time Series
```
GET /public/coins/:coin/time-series/v2
```
Get historical market and social data for a coin.

**Parameters:**
- `coin` (required): Coin ID or symbol
- `bucket`: Data grouping ('hour' or 'day')
- `interval`: Time interval
- `start`: Start timestamp
- `end`: End timestamp

### Creators

#### 1. List Creators
```
GET /public/creators/list/v1
```
Get trending social creators based on interactions.

**Response Fields:**
- `creator_name`: Username
- `creator_display_name`: Display name
- `creator_id`: Unique identifier
- `creator_network`: Social network
- `creator_followers`: Follower count
- `interactions_24h`: 24-hour interactions

#### 2. Creator Details
```
GET /public/creator/:network/:id/v1
```
Get detailed information about a specific creator.

**Parameters:**
- `network` (required): Social network (twitter, youtube, instagram, reddit, tiktok)
- `id` (required): Creator's unique ID or username

## Rate Limits
Some endpoints require the professional plan with upgraded API access. Contact LunarCrush for specific rate limit information.

## Notes
- Times are in Unix timestamps (seconds)
- Social data typically covers the last 24 hours unless specified
- Market data is real-time or near real-time
- Some features require professional plan subscription