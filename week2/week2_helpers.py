# Reference: https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python 


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