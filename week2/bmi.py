import math

def validate_positive(measurement):
    if measurement <= 0:
        raise ValueError

def calculate_bmi():
    try:
        weight_in_kg = float(input('Enter weight in kilograms: '))
        validate_positive(weight_in_kg)
        height_in_cm = float(input('Enter height in centimetres: '))
        validate_positive(height_in_cm)
        bmi = weight_in_kg / math.pow((height_in_cm / 100), 2)
        print('BMI is ' + str(round(bmi, 2)))
    except(ValueError):
        print('Invalid value entered. You must enter a number greater than 0')
    finally:
        choice = input('Enter any key to try again, or enter "exit" (case-sensitive) to quit')
        if choice == 'exit':
            print('Goodbye')
        else:
           calculate_bmi() 

calculate_bmi()