from decimal import Decimal
import unittest
from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse

from crypto.models import Currency


class AggregatedDataTests(TestCase):

    def setUp(self):
        # Set up initial data
        Currency.objects.create(symbol='BTC')
        Currency.objects.create(symbol='ETH')

        # Create a client instance
        self.client = Client()

    @patch('crypto.views.fetch_prices')
    def test_aggregated_data_default(self, mock_fetch_prices):
        # Mock fetch_prices to return controlled test data
        mock_fetch_prices.return_value = (31000, 31038.9)  # Mocked prices for Coinbase and Bitstamp

        # Test aggregated data with default amount
        response = self.client.get(reverse('aggregated_data'))
        self.assertEqual(response.status_code, 200)
        data = response.json()['aggregated_data']
        btc_profit = next((item for item in data if item['symbol'] == 'BTC'), None)['profit']
        eth_profit = next((item for item in data if item['symbol'] == 'ETH'), None)['profit']
        self.assertEqual(btc_profit, '38.90', msg="BTC profit per 1 unit")
        self.assertEqual(eth_profit, '38.90', msg="ETH profit per 1 unit")

    @patch('crypto.views.fetch_prices')
    def test_aggregated_data_custom_amount(self, mock_fetch_prices):
        # Mock fetch_prices to return controlled test data
        mock_fetch_prices.return_value = (31000, 31038.9)  # Mocked prices for Coinbase and Bitstamp

        # Test aggregated data with custom amount
        response = self.client.post(reverse('aggregated_data'), {'amount': 2})
        self.assertEqual(response.status_code, 200)
        data = response.json()['aggregated_data']
        btc_profit = next((item for item in data if item['symbol'] == 'BTC'), None)['profit']
        eth_profit = next((item for item in data if item['symbol'] == 'ETH'), None)['profit']
        self.assertEqual(btc_profit, '77.80', msg="BTC profit for amount 2")
        self.assertEqual(eth_profit, '77.80', msg="ETH profit for amount 2")

    @patch('crypto.views.fetch_prices')
    def test_calculate_profit_api(self, mock_fetch_prices):
        # Mock fetch_prices to return controlled test data
        mock_fetch_prices.return_value = (31000, 31038.9)  # Mocked prices for Coinbase and Bitstamp

        # Test calculate profit API
        response = self.client.get(reverse('calculate_profit', args=[2]))
        self.assertEqual(response.status_code, 200)
        data = response.json()['aggregated_data']
        btc_profit = next(item['profit'] for item in data if item['symbol'] == 'BTC')
        eth_profit = next(item['profit'] for item in data if item['symbol'] == 'ETH')
        self.assertEqual(btc_profit, '77.80', msg="BTC profit for amount 2")
        self.assertEqual(eth_profit, '77.80', msg="ETH profit for amount 2")


# Run the tests
if __name__ == "__main__":
    unittest.main()