from django.http import JsonResponse

from crypto.models import Currency
from crypto.views import fetch_prices


def calculate_profit(request, amount):
    coinbase_data, bitstamp_data = fetch_prices()
    opportunities = []

    for currency in Currency.objects.all():
        coinbase_price = coinbase_data.get(currency.symbol, 0)
        bitstamp_price = bitstamp_data.get(currency.symbol, 0)

        if coinbase_price and bitstamp_price:
            profit = (float(bitstamp_price) - float(coinbase_price)) * amount
            opportunities.append({
                'symbol': currency.symbol,
                'buy_from': 'Coinbase',
                'sell_to': 'Bitstamp',
                'profit': "{:.10f}".format(profit)  # Format profit to fixed precision
            })

    return JsonResponse({'aggregated_data': opportunities})

