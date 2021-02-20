# Reference: https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python 
# Reference: https://book.pythontips.com/en/latest/ternary_operators.html
# Reference: https://www.kite.com/python/answers/how-to-check-internet-connection-in-python
import requests


# Method Signature: in_permitted_float_range
# Params: input, min, max
# Description: Checks that input, min and max are of type float. Returns true if input is in-between min & max, false otherwise
def in_permitted_float_range(input, min, max):

    param_dict = {
        'Input': input,
        'Minimum': min,
        'Maximum': max
    }

    for key, value in param_dict.items():
        if not parse_float(value):
            print(error_msg(f'{key} cannot be converted to a decimal'))
            return False
        
    if float(input) <= min:
        print(error_msg(f'Input cannot be less than or equal to {min}'))
        return False

    if float(input) > max:
        print(error_msg(f'Input cannot be greater than {max}'))
        return False

    return True


# Method Signature:   in_permitted_int_range
# Params:   input, min, max
# Description:   The int equivalent to method 'in_float_range' (see above)
def in_permitted_int_range(input, min, max):

    param_dict = {
        'Input': input,
        'Minimum': min,
        'Maximum': max
    }

    for key, value in param_dict.items():
        if not parse_int(value):
            print(error_msg(f'{key} cannot be converted to an integer'))
            return False
        
    if int(input) <= min:
        print(error_msg(f'Input cannot be less than or equal to {min}'))
        return False

    if int(input) > max:
        print(error_msg(f'Input cannot be greater than {max}'))
        return False

    return True


# Method Signature:  positive_float_difference
# Params:   float1, float2
# Description:   Finds the greatest of two floating point numbers and subtracts smallest from the greatest to return the positive difference between the two
def positive_float_difference(float1, float2):
    if not parse_float(float1):
        print(error_msg('Argument 1 of "positive_float_difference()" cannot be parsed to a float'))
        return None
    if not parse_float(float2):
        print(error_msg('Argument 2 of "positive_float_difference()" cannot be parsed to a float'))
        return None
    return (float1 - float2, float2 - float1)[float1 <= float2]


# Method Signature:   do_not_replay
# Params:   
# Description:   Prompts the user to re-use the program to which it is appended 
def do_not_replay():
    choice = input('\nEnter any key to try again, or enter "exit" (case-insensitive) to quit:   ')
    if choice.upper() == 'EXIT':
        print('\nGoodbye')
        return True
    else:
        return False


# Method Signature:   http_status
# Params:   
# Description:   Checks the reponse code for a given http request. Returns true if request successful, false otherwise. Prints appropriate message.
def http_request_successful(response_code):
    return response_code == 200


# Method Signature:   internet_connection_present
# Params:   
# Description:   Returns true if the user is connected to the internet, false otherwise
def internet_connection_present(url):
    timeout = 5
    try:
        requests.get(url, timeout = timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        print(error_msg("No internet connection."))
        return False


# Method Signature:   error_msg
# Params:   output
# Description:   Prepends an error prefix onto a string to mark said string as an error message
def error_msg(output):
    if parse_str(output):
        return '\nERROR: ' + output
    return '\nERROR: parameter "output" in of method "errorMsg() cannot be parsed to a string"'


# Method Signature:   parse_float
# Params:   input
# Description:   Returns true if input can be parsed to a float, false otherwise
def parse_float(input):
    try:
        float(input)
        return True
    except ValueError:
        return False


# Method Signature:   parse_bool
# Params:   input
# Description:   The boolean equivalent to method 'parse_float' (see above)
def parse_bool(input):
    try:
        bool(input)
        return True
    except ValueError:
        return False


# Method Signature:   parse_str
# Params:   input
# Description:   The string equivalent to method 'parse_float' (see above)
def parse_str(input):
    try:
        str(input)
        return True
    except ValueError:
        return False


# Method Signature:   parse_int
# Params:   input
# Description:   The int equivalent to method 'parse_float' (see above)
def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False
    
