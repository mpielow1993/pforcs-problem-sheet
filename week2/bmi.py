import math, helper_methods as help

# Method:   calculate_bmi()   
# Description: Calculates a value for Body Mass Index based on user inputs for weight and height
def calculate_bmi(): 
    # Set realistic limits for height and weight
    weight_limits = {
        'min': 0,
        'max': 200
    }
    height_limits = {
        'min': 0,
        'max': 300
    }    
    weight_in_kg = input(f'\nEnter weight in kilograms.\nMinimum is {weight_limits["min"]}. Maximum is {weight_limits["max"]}:   ')
    if help.in_permitted_range(weight_in_kg, weight_limits["min"], weight_limits["max"], float):
        height_in_cm = input(f'\nEnter height in centimetres.\nMinimum is {height_limits["min"]}. Maximum is {height_limits["max"]}:   ')
        if help.in_permitted_range(height_in_cm, height_limits["min"], height_limits["max"], float):
            bmi = float(weight_in_kg) / math.pow((float(height_in_cm) / 100), 2)
            print(f'\nBMI is {str(round(bmi, 2))}')
    if not help.do_not_replay():
        calculate_bmi()