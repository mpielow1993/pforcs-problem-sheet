def calculate_bmi():
    try:
        weight_in_kg = input('Enter weight in kilograms:   ')
        weight_in_kg = int(weight_in_kg)
        height_in_cm = input('Enter height in centimetres:   ')
        height_in_cm = int(height_in_cm)
        height_in_m = height_in_cm / 100
        bmi = weight_in_kg / height_in_m
        print('BMI is ' + str(bmi))
    except(TypeError, ValueError):
        print('Invalid value entered')

calculate_bmi()