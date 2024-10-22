# LunarCrush API Usage Guide

## Authentication Setup

Before making any requests, you'll need your API key from LunarCrush.

### JavaScript Setup
```javascript
const LUNARCRUSH_API_KEY = 'your_api_key_here';
const BASE_URL = 'https://lunarcrush.com/api4';

// Default headers for fetch requests
const headers = {
    'Authorization': `Bearer ${LUNARCRUSH_API_KEY}`
};
```

### Python Setup
```python
import requests

LUNARCRUSH_API_KEY = 'your_api_key_here'
BASE_URL = 'https://lunarcrush.com/api4'

# Default headers for requests
headers = {
    'Authorization': f'Bearer {LUNARCRUSH_API_KEY}'
}
```

## Common API Calls

### 1. Get Trending Topics

#### JavaScript
```javascript
// Using fetch
async function getTrendingTopics() {
    try {
        const response = await fetch(`${BASE_URL}/public/topics/list/v1`, { headers });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching trending topics:', error);
        throw error;
    }
}

// Using axios
const axios = require('axios');

async function getTrendingTopicsAxios() {
    try {
        const response = await axios.get(`${BASE_URL}/public/topics/list/v1`, { headers });
        return response.data;
    } catch (error) {
        console.error('Error fetching trending topics:', error);
        throw error;
    }
}
```

#### Python
```python
def get_trending_topics():
    try:
        response = requests.get(f"{BASE_URL}/public/topics/list/v1", headers=headers)
        response.raise_for_status()  # Raises an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trending topics: {e}")
        raise
```

### 2. Get Coin Details

#### JavaScript
```javascript
async function getCoinDetails(coinId) {
    try {
        const response = await fetch(`${BASE_URL}/public/coins/${coinId}/v1`, { headers });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(`Error fetching coin details for ${coinId}:`, error);
        throw error;
    }
}

// Example usage
getCoinDetails('BTC').then(data => {
    console.log('Bitcoin Details:', data);
});
```

#### Python
```python
def get_coin_details(coin_id):
    try:
        response = requests.get(f"{BASE_URL}/public/coins/{coin_id}/v1", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coin details for {coin_id}: {e}")
        raise

# Example usage
bitcoin_details = get_coin_details('BTC')
print('Bitcoin Details:', bitcoin_details)
```

### 3. Get Time Series Data

#### JavaScript
```javascript
async function getTimeSeries(coin, params = {}) {
    const queryParams = new URLSearchParams({
        bucket: params.bucket || 'hour',
        interval: params.interval || '1w',
        ...params
    }).toString();

    try {
        const response = await fetch(
            `${BASE_URL}/public/coins/${coin}/time-series/v2?${queryParams}`, 
            { headers }
        );
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(`Error fetching time series for ${coin}:`, error);
        throw error;
    }
}

// Example usage
getTimeSeries('BTC', {
    bucket: 'day',
    interval: '1m'
}).then(data => {
    console.log('Bitcoin Time Series:', data);
});
```

#### Python
```python
def get_time_series(coin, **params):
    default_params = {
        'bucket': 'hour',
        'interval': '1w'
    }
    # Update default params with any provided params
    params = {**default_params, **params}
    
    try:
        response = requests.get(
            f"{BASE_URL}/public/coins/{coin}/time-series/v2",
            headers=headers,
            params=params
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching time series for {coin}: {e}")
        raise

# Example usage
btc_time_series = get_time_series('BTC', bucket='day', interval='1m')
print('Bitcoin Time Series:', btc_time_series)
```

### 4. Get Creator Analytics

#### JavaScript
```javascript
async function getCreatorAnalytics(network, creatorId) {
    try {
        const response = await fetch(
            `${BASE_URL}/public/creator/${network}/${creatorId}/v1`,
            { headers }
        );
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(`Error fetching creator analytics:`, error);
        throw error;
    }
}

// Example usage
getCreatorAnalytics('twitter', 'elonmusk').then(data => {
    console.log('Creator Analytics:', data);
});
```

#### Python
```python
def get_creator_analytics(network, creator_id):
    try:
        response = requests.get(
            f"{BASE_URL}/public/creator/{network}/{creator_id}/v1",
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching creator analytics: {e}")
        raise

# Example usage
creator_data = get_creator_analytics('twitter', 'elonmusk')
print('Creator Analytics:', creator_data)
```

## Error Handling and Best Practices

### JavaScript Error Handling
```javascript
async function makeApiRequest(endpoint) {
    try {
        const response = await fetch(`${BASE_URL}${endpoint}`, { headers });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        if (error.name === 'AbortError') {
            console.error('Request was aborted');
        } else if (error.name === 'TypeError') {
            console.error('Network error');
        } else {
            console.error('Other error:', error.message);
        }
        throw error;
    }
}
```

### Python Error Handling
```python
def make_api_request(endpoint):
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting to the server: {conn_err}")
        raise
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
        raise
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        raise
```

## Rate Limiting and Optimization

### JavaScript Implementation
```javascript
class RateLimiter {
    constructor(requestsPerSecond = 1) {
        this.queue = [];
        this.requestsPerSecond = requestsPerSecond;
        this.lastRequestTime = 0;
    }

    async request(endpoint) {
        const now = Date.now();
        const timeToWait = Math.max(0, (1000 / this.requestsPerSecond) - (now - this.lastRequestTime));
        
        await new Promise(resolve => setTimeout(resolve, timeToWait));
        
        this.lastRequestTime = Date.now();
        return await makeApiRequest(endpoint);
    }
}

// Usage
const rateLimiter = new RateLimiter(2); // 2 requests per second
rateLimiter.request('/public/topics/list/v1').then(data => {
    console.log(data);
});
```

### Python Implementation
```python
import time
from functools import wraps

def rate_limit(calls_per_second=1):
    min_interval = 1.0 / calls_per_second
    last_call_time = 0

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call_time
            current_time = time.time()
            time_since_last_call = current_time - last_call_time
            
            if time_since_last_call < min_interval:
                time.sleep(min_interval - time_since_last_call)
            
            last_call_time = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Usage
@rate_limit(calls_per_second=2)
def get_topics():
    return make_api_request('/public/topics/list/v1')
```

## Data Processing Examples

### JavaScript
```javascript
async function analyzeCoinTrends(coinId) {
    const data = await getCoinDetails(coinId);
    
    // Calculate basic metrics
    const metrics = {
        priceChange24h: data.percent_change_24h,
        marketCapRank: data.market_cap_rank,
        socialScore: data.galaxy_score,
        volatilityIndex: data.volatility
    };
    
    return metrics;
}
```

### Python
```python
def analyze_coin_trends(coin_id):
    data = get_coin_details(coin_id)
    
    # Calculate basic metrics
    metrics = {
        'price_change_24h': data['percent_change_24h'],
        'market_cap_rank': data['market_cap_rank'],
        'social_score': data['galaxy_score'],
        'volatility_index': data['volatility']
    }
    
    return metrics
```