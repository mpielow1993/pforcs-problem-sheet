# Reference: https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python 

# Method:   parse_int()
# Params:   input
# Description:   The int equivalent to method 'parse_float' of week2_helpers.py
def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


# Method: in_int_range()
# Params: input, min, max
# Description:   The int equivalent to method 'in_float_range' of week2_helpers.py
def in_int_range(input, min, max):

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