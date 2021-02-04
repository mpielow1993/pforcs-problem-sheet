import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
data = requests.get(url).json()

# Format the float value of the retrieved rate into USD format
# Reference: 'https://www.kite.com/python/answers/how-to-format-a-float-as-currency-in-python'
one_btc_in_usd = "${:,.2f}".format(float(data["bpi"]["USD"]["rate_float"]))
print('1 BTC = ' + one_btc_in_usd)