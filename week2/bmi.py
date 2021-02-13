import math
from week2 import week2_helpers as w2h

def calculate_bmi():
    # Set realistic limits for height and weight
    weight_in_kg = input('\nEnter weight in kilograms: ')
    if w2h.in_float_range(weight_in_kg, 0, 500):
        height_in_cm = input('\nEnter height in centimetres: ')
        if w2h.in_float_range(height_in_cm, 0, 300):
            bmi = float(weight_in_kg) / math.pow((float(height_in_cm) / 100), 2)
            print(f'\nBMI is {str(round(bmi, 2))}')
    choice = input('\nEnter any key to try again, or enter "exit" (case-sensitive) to quit:   ')
    if choice == 'exit':
        print('\nGoodbye')
    else:
        calculate_bmi()