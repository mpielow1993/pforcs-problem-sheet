import requests, helper_methods as help

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
        
        if help.internet_connection_present(url):

            data = requests.get(url)

            if help.http_request_successful(data.status_code):
                data = data.json()
                print('\n1 BTC = ' + available_currencies[input_currency] + "{:,.2f}".format(float(data["bpi"][input_currency]["rate_float"])))
            else:
                print(help.error_msg(f'HTTP request to "{url}" unsuccessful'))
    else:
        print(help.error_msg('Input is not equal to any one of the listed currencies'))
    
    if not help.do_not_replay():
        get_current_bitcoin_price() 
