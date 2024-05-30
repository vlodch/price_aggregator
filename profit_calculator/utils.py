# profit_calculator/utils.py

def calculate_profit(currencies):
    profit_results = {}
    for currency in currencies:
        profit = calculate_profit_for_currency(currency)
        profit_results[currency.name] = profit
    return profit_results


def calculate_profit_for_currency(currency):
    # Fetching data from the database and calculating profits
    # Example:
    buy_price = currency.buy_price
    sell_price = currency.sell_price
    profit = sell_price - buy_price

    # Assuming profit is a field in the Currency model, update it
    currency.profit = profit
    currency.save()

    return profit
s