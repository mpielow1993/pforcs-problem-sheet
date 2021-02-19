import math, helpers

def calculate_bmi():
    # Set realistic limits for height and weight
    weight_limits = {
        'min': 0,
        'max': 500
    }

    height_limits = {
        'min': 0,
        'max': 300
    }    

    weight_in_kg = input('\nEnter weight in kilograms: ')
    if helpers.in_permitted_float_range(weight_in_kg, weight_limits["min"], weight_limits["max"]):
        height_in_cm = input('\nEnter height in centimetres: ')
        if helpers.in_permitted_float_range(height_in_cm, height_limits["min"], height_limits["max"]):
            bmi = float(weight_in_kg) / math.pow((float(height_in_cm) / 100), 2)
            print(f'\nBMI is {str(round(bmi, 2))}')
    choice = input('\nEnter any key to try again, or enter "exit" (case-sensitive) to quit:   ')
    if choice == 'exit':
        print('\nGoodbye')
    else:
        calculate_bmi()