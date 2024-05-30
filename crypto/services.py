import requests
from decimal import Decimal


def fetch_coinbase_price(symbol):
    url = f"https://api.coinbase.com/v2/prices/{symbol}-USD/spot"
    response = requests.get(url)
    data = response.json()
    return Decimal(data['data']['amount'])


def fetch_bitstamp_price(symbol):
    url = f"https://www.bitstamp.net/api/v2/ticker/{symbol.lower()}usd"
    response = requests.get(url)
    data = response.json()
    return Decimal(data['last'])


def fetch_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT"
    response = requests.get(url)
    data = response.json()
    return Decimal(data['price'])


def fetch_prices(symbol):
    coinbase_price = fetch_coinbase_price(symbol)
    bitstamp_price = fetch_bitstamp_price(symbol)
    binance_price = fetch_binance_price(symbol)
    return coinbase_price, bitstamp_price, binance_price
