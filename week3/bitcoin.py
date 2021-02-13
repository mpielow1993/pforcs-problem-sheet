import requests

def convert_one_btc_to_usd():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    data = requests.get(url).json()

    # Format the float value of the retrieved rate into USD format
    # Reference: 'https://www.kite.com/python/answers/how-to-format-a-float-as-currency-in-python'
    print(f'1 BTC = {"${:,.2f}".format(float(data["bpi"]["USD"]["rate_float"]))}')