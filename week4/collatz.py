import helpers

def collatz():

    limits = {
        'min': 1,
        'max': 1000
    }

    input_str = input(f'\nEnter any positive integer greater than {limits["min"]} and less than or equal to {limits["max"]}:   ')
    # Maximum allowed integer is 100 here for demo, but can be set higher if desired
    if helpers.in_permitted_int_range(input_str, limits["min"], limits["max"]):
        result_str = input_str
        input_int = int(input_str)
        while input_int != 1:
            if input_int % 2 == 0:
                input_int /= 2
            else:
                input_int = input_int * 3 + 1
            # Remove trailing zeros for final output
            # Reference:   https://www.kite.com/python/answers/how-to-remove-leading-and-trailing-zeros-in-a-string-in-python
            result_str += str(f' {input_int}').strip('.0')
        print(result_str)
    choice = input('\nEnter any key to try again, or enter "exit" (case-sensitive) to quit:   ')
    if choice == 'exit':
        print('\nGoodbye')
    else:
        collatz() 