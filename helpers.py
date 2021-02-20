# Reference: https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python 
# Reference: https://book.pythontips.com/en/latest/ternary_operators.html



# Method Signature:   parse_float
# Params:   input
# Description:   Returns true if input can be parsed to a float, false otherwise
def parse_float(input):
    try:
        float(input)
        return True
    except ValueError:
        return False


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
            print(f'\nERROR: {key} cannot be converted to a decimal')
            return False
        
    if float(input) <= min:
        print(f'\nERROR: Input cannot be less than or equal to {min}')
        return False

    if float(input) > max:
        print(f'\nERROR: Input cannot be greater than {max}')
        return False

    return True


# Method Signature:   parse_int
# Params:   input
# Description:   The int equivalent to method 'parse_float' (see above)
def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


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
            print(f'\nERROR: {key} cannot be converted to an integer')
            return False
        
    if int(input) <= min:
        print(f'\nERROR: Input cannot be less than or equal to {min}')
        return False

    if int(input) > max:
        print(f'\nERROR: Input cannot be greater than {max}')
        return False

    return True


# Method Signature:  positive_float_difference
# Params:   float1, float2
# Description:   Finds the greatest of two floating point numbers and subtracts smallest from the greatest to return the positive difference between the two
def positive_float_difference(float1, float2):
    if not parse_float(float1):
        print('ERROR: Argument 1 of "positive_float_difference()" cannot be parsed to a float')
        return None
    if not parse_float(float2):
        print('ERROR: Argument 2 of "positive_float_difference()" cannot be parsed to a float')
        return None
    return (float1 - float2, float2 - float1)[float1 <= float2]


# Method Signature:   parse_bool
# Params:   input
# Description:   Returns true if input can be parsed to a boolean, false otherwise
def parse_bool(input):
    try:
        bool(input)
        return True
    except ValueError:
        return False


# Method Signature:   parse_bool
# Params:   
# Description:   Prompts the user to re-use the program to which it is appended 
def do_not_replay():
    choice = input('\nEnter any key to try again, or enter "exit" (case-insensitive) to quit:   ')
    if choice.upper() == 'EXIT':
        print('\nGoodbye')
        return True
    else:
        return False
