import helper_methods as help


# Method Signature:   estimate_sqrt
# Params:   step
# Description: Estimates the square root of a positive integer by repeatedly incrementing a given step value
def estimate_sqrt(step = 0.01):
    
    # set a realistic step value
    # note in_permitted_float_range will return false for step <= minimum (so the while loop below will definitely terminate)
    help.in_permitted_float_range(step, 0, 1)
    
    limits = {
        'min': 0.01,
        'max': 1000
    }
    
    squared_number = input(f'Enter a positive number to estimate its positive square root. \n(Minimum is {limits["min"]}. Maximum is {limits["max"]}):   ')

    if help.in_permitted_float_range(squared_number, limits['min'], limits['max']):

        squared_number = float(squared_number)
        square_root = 0
        initial_estimate = square_root * square_root

        while (True):
            initial_error = help.positive_float_difference(initial_estimate, squared_number)
            square_root += step
            final_estimate = square_root * square_root
            final_error = help.positive_float_difference(final_estimate, squared_number)
            if (final_error >= initial_error):
                break
            initial_estimate = final_estimate

        print(f'The square root of {squared_number} is approximately {square_root}')
    
    if not help.do_not_replay():
        estimate_sqrt(step)

        
    