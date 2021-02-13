from week4 import week4_helpers as w4h

def collatz():
    input_str = input('\nEnter any positive integer:   ')
    # Maximum allowed integer is 100 here for demo, but can be set higher if desired
    if w4h.in_int_range(input_str, 0, 100):
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