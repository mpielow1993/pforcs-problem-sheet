import requests, helper_methods as help

# Method:   get_current_bitcoin_price()
# Description:  Calculates the current value of 1 bitcoin selected by the user from a given collection
def get_current_bitcoin_price():
    available_currencies = {
        'USD': '$',
        'GBP': '£',
        'EUR': '€'
    }
    input_currency = input(f'Enter any one of the following currencies (case-insensitive) to get the value of 1 bitcoin for that currency:\n({", ".join(available_currencies.keys())})   ')
    input_currency = input_currency.upper()
    if help.is_valid_answer(input_currency, available_currencies.keys()):
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
