from week5 import week5_helpers as w5h

def estimate_sqrt(step):
    
    # set a realistic step value
    w5h.in_float_range(step, 0, 1)
    
    limits = {
        'min': 0.01,
        'max': 1000
    }
    
    squared_number = input(f'Enter a positive number to estimate its positive square root. \n(Minimum is {limits["min"]}. Maximum is {limits["max"]}):   ')

    if w5h.in_float_range(squared_number, limits['min'], limits['max']):

        squared_number = float(squared_number)
        square_root = 0
        initial_estimate = square_root * square_root

        while (True):
            initial_error = w5h.positive_float_difference(initial_estimate, squared_number)
            #print(initial_error)
            square_root += step
            final_estimate = square_root * square_root
            final_error = w5h.positive_float_difference(final_estimate, squared_number)
            #print(final_error)
            if (final_error >= initial_error):
                break
            initial_estimate = final_estimate

        print(f'The square root of {squared_number} is approximately {square_root}')
    
    choice = input('\nEnter any key to try again, or enter "exit" (case-sensitive) to quit:   ')
    if choice == 'exit':
        print('\nGoodbye')
    else:
        estimate_sqrt(step)

        
    