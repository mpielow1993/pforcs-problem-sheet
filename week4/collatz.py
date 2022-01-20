# Reference:   https://www.kite.com/python/answers/how-to-remove-leading-and-trailing-zeros-in-a-string-in-python

import helper_methods as help

# Method:   collatz()
# Description:  Accepts a positive integer input by the user. 
#   Performs calculations in the following fashion:
#       Outputs the result each time until a value of 1 is reached.
#       If the value is even - divides by 2
#       If the value is odd - multiplies by 3 and adds 1
def collatz():
    limits = {
        'min': 1,
        'max': 1000
    }
    input_str = input(f'\nEnter any positive integer greater than {limits["min"]} and less than or equal to {limits["max"]}:   ')
    # Maximum allowed integer is 100 here for demo, but can be set higher if desired
    if help.in_permitted_range(input_str, limits["min"], limits["max"], int):
        result_str = input_str
        input_int = int(input_str)
        while input_int != 1:
            if input_int % 2 == 0:
                input_int /= 2
            else:
                input_int = input_int * 3 + 1
            # Remove trailing zeros for final output
            result_str += str(f' {input_int}').strip('.0')
        print(result_str)  
    if not help.do_not_replay():
        collatz()