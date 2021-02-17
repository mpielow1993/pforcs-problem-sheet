# *************************************************************************************

# DUPLICATED FROM 'week2_helpers.py'

# *************************************************************************************

# Signature: positive_float_difference(float1, float2)
# Params:   input
# Description:   Finds the greatest of two floating point numbers and subtracts the other from to return the positive difference
def positive_float_difference(float1, float2):
    if not parse_float(float1):
        print('ERROR: Argument 1 of "positive_float_difference()" cannot be parsed to a float')
    if not parse_float(float2):
        print('ERROR: Argument 2 of "positive_float_difference()" cannot be parsed to a float')
    return (float1 - float2, float2 - float1)[float1 <= float2]


# Signature:   parse_bool()
# Params:   input
# Description:   Returns true if input can be parsed to a boolean, false otherwise
def parse_bool(input):
    try:
        bool(input)
        return True
    except ValueError:
        return False


# Signature:   parse_float()
# Params:   input
# Description:   Returns true if input can be parsed to a float, false otherwise
def parse_float(input):
    try:
        float(input)
        return True
    except ValueError:
        return False


# Method: in_float_range()
# Params: input, min, max
# Description:   Checks that input, min and max are of type float. Returns true if input is in-between min & max, false otherwise
def in_float_range(input, min, max):

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