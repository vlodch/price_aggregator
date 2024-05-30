# profit_calculator/profit_calculator.py

from .models import ProfitCurrency  # Import the renamed Currency model


def calculate_profit(buy_platform, sell_platform):
    currencies = ProfitCurrency.objects.filter(buy_platform=buy_platform, sell_platform=sell_platform)
    if currencies.exists():
        total_profit = currencies.aggregate(total_profit=models.Sum('profit'))['total_profit']
        return total_profit if total_profit else 0
    else:
        return 0
