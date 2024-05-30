from django.shortcuts import render
from django.http import JsonResponse
from .models import Currency
from .services import fetch_prices
from decimal import Decimal, InvalidOperation
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'crypto/index.html')


def calculate_profit(request, symbol, amount):
    try:
        amount = Decimal(amount)
    except InvalidOperation:
        return JsonResponse({'error': 'Invalid amount'}, status=400)

    try:
        coinbase_price, bitstamp_price, binance_price = fetch_prices(symbol)

        profits = [
            ('Coinbase', 'Bitstamp', (bitstamp_price - coinbase_price) * amount),
            ('Coinbase', 'Binance', (binance_price - coinbase_price) * amount),
            ('Bitstamp', 'Binance', (binance_price - bitstamp_price) * amount),
        ]

        profitable_combinations = [p for p in profits if p[2] > 0]
        if profitable_combinations:
            best_buy_platform, best_sell_platform, max_profit = max(profitable_combinations, key=lambda x: x[2])
            result = {
                'symbol': symbol,
                'amount': f'{amount:.2f}',
                'best_buy_platform': best_buy_platform,
                'best_sell_platform': best_sell_platform,
                'max_profit': f'{max_profit:.10f}'
            }
        else:
            result = {'message': 'No profitable trading opportunity'}

        return JsonResponse(result)
    except Exception as e:
        logger.error(f"Error calculating profit: {e}")
        return JsonResponse({'error': str(e)}, status=400)


def aggregated_data_view(request):
    aggregated_data = []

    if request.method == "POST":
        try:
            amount = Decimal(request.POST.get('amount', '1'))
        except InvalidOperation:
            amount = Decimal(1)

        currencies = Currency.objects.all()

        for currency in currencies:
            try:
                coinbase_price, bitstamp_price, binance_price = fetch_prices(currency.symbol)
                profits = [
                    ('Coinbase', 'Bitstamp', (bitstamp_price - coinbase_price) * amount),
                    ('Coinbase', 'Binance', (binance_price - coinbase_price) * amount),
                    ('Bitstamp', 'Binance', (binance_price - bitstamp_price) * amount),
                ]

                profitable_combinations = [p for p in profits if p[2] > 0]

                if profitable_combinations:
                    best_buy_platform, best_sell_platform, max_profit = max(profitable_combinations, key=lambda x: x[2])
                    aggregated_data.append({
                        'symbol': currency.symbol,
                        'coinbase_price': f'{coinbase_price:.2f}',
                        'bitstamp_price': f'{bitstamp_price:.2f}',
                        'binance_price': f'{binance_price:.2f}',
                        'best_buy_platform': best_buy_platform,
                        'best_sell_platform': best_sell_platform,
                        'max_profit': f'{max_profit:.10f}'
                    })
                else:
                    logger.info(f"No profitable combination for {currency.symbol}")
            except Exception as e:
                logger.error(f"Error fetching prices for {currency.symbol}: {str(e)}")
                continue

    return render(request, 'crypto/aggregated_data.html', {'aggregated_data': aggregated_data})
