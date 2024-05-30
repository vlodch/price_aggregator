from IPython.display import display, HTML

def display_best_trading_opportunities(data, symbols):
    """
    Displays the best trading opportunities based on the fetched prices and calculated profits.

    Args:
    - data (dict): A dictionary containing the fetched prices and calculated profits.
    - symbols (list): A list of symbols for cryptocurrencies.
    """
    profits = data['profits']

    best_trades = {symbol: max(profits[symbol], key=lambda x: x['profit']) for symbol in profits}

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Best Trading Opportunities (Profit per 1 {symbols[0]})</title>
        <style>
            table, th, td {{
                border: 1px solid black;
                border-collapse: collapse;
                padding: 8px;
            }}
        </style>
    </head>
    <body>
        <h1>Best Trading Opportunities (Profit per 1 {symbols[0]})</h1>
        <table>
            <tr>
                <th>Cryptocurrency</th>
                <th>Buy From</th>
                <th>Sell To</th>
                <th>Profit</th>
            </tr>
    """
    for symbol in best_trades:
        html_content += f"""
            <tr>
                <td>{symbol}</td>
                <td>{best_trades[symbol]['buy_from']}</td>
                <td>{best_trades[symbol]['sell_to']}</td>
                <td>{best_trades[symbol]['profit']:.10f}</td>  # Adjust the precision here
            </tr>
        """
    html_content += """
        </table>
    </body>
    </html>
    """

    display(HTML(html_content))
