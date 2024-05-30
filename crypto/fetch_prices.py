import requests
from decimal import Decimal
import logging

# Configure logging
logger = logging.getLogger(__name__)


def fetch_prices(symbol):
    platforms = [
        {'name': 'Coinbase', 'url': 'https://api.coinbase.com/v2/prices/spot?currency=USD'},
        {'name': 'Bitstamp', 'url': 'https://www.bitstamp.net/api/v2/ticker/btcusd/'},
        {'name': 'Binance', 'url': 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'},
        # Add more platforms here if needed
    ]

    prices = {}
    for platform in platforms:
        try:
            response = requests.get(platform['url'])
            if response.status_code == 200:
                data = response.json()
                price = Decimal(data.get('data', {}).get('amount', 0))
                prices[platform['name']] = price
                logger.info(f"Fetched price from {platform['name']}: {price}")
            else:
                logger.warning(f"Failed to fetch data from {platform['name']}: {response.status_code}")
        except Exception as e:
            logger.error(f"Error fetching data from {platform['name']}: {e}")

    return prices.get('Coinbase', Decimal(0)), prices.get('Bitstamp', Decimal(0)), prices.get('Binance', Decimal(0))
