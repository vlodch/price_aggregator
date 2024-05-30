# crypto/management/commands/populate_currencies.py

from django.core.management.base import BaseCommand
from crypto.models import Currency


class Command(BaseCommand):
    help = 'Populate the Currency table with initial data'

    def handle(self, *args, **kwargs):
        currencies = [
            {"symbol": "BTC", "buy_from": "Coinbase", "sell_to": "Bitstamp", "buy_price": 0},
            {"symbol": "ETH", "buy_from": "Coinbase", "sell_to": "Bitstamp", "buy_price": 0},
            {"symbol": "LTC", "buy_from": "Coinbase", "sell_to": "Bitstamp", "buy_price": 0},
            # Add other currencies as needed
        ]

        for currency in currencies:
            Currency.objects.create(**currency)

        self.stdout.write(self.style.SUCCESS('Successfully populated Currency table'))
