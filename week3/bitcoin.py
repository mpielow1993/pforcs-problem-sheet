import requests, helpers

# Method Signature:   convert_one_bitcoin_to_usd
# Params:   
# Description: Calculates the current value of 1 bitcoin is USD
def get_current_bitcoin_price():

    available_currencies = {
        'USD': '$',
        'GBP': '£',
        'EUR': '€'
    }

    input_currency = input('Enter any one of the following currencies (case-insensitive) to get the value of 1 bitcoin for that currency:\n(USD, GBP, EUR)   ')
    input_currency = input_currency.upper()

    if input_currency in available_currencies.keys():
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        data = requests.get(url).json()
        print('\n1 BTC = ' + available_currencies[input_currency] + "{:,.2f}".format(float(data["bpi"][input_currency]["rate_float"])))
    else:
        print('\nERROR: Input is not equal to any one of the listed currencies')
    
    if not helpers.do_not_replay():
        get_current_bitcoin_price() 
