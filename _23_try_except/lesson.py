import requests
import time

try:
    url = 'https://api.binance.com/api/v3/ticker/price'

    bitcoin_prices = []
    for i in range(2):
        response = requests.get(url, params={'symbol': 'BTCUSDT'})
        price = float(response.json()['price'])
        bitcoin_prices.append(price)
        time.sleep(1)

    print(bitcoin_prices)
    print(len(bitcoin_prices))
    print(max(bitcoin_prices))
    print(min(bitcoin_prices))
except requests.exceptions.ConnectionError as error:
    print(f"something goes wrong: {error}")