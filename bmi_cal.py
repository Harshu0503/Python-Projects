def calculate_bmi(weight, height):
    try:
        # Convert height from centimeters to meters
        height_in_meters = height / 100.0

        # Calculate BMI using the formula
        bmi = weight / (height_in_meters ** 2)

        return bmi
    except ZeroDivisionError:
        return "Error: Height cannot be zero."

# Get user input for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

# Calculate BMI
result = calculate_bmi(weight, height)

# Display the result
if isinstance(result, float):
    print("Your BMI is {:.2f}".format(result))
    if result < 18.5:
        print("Underweight")
    elif 18.5 <= result < 25:
        print("Normal weight")
    elif 25 <= result < 30:
        print("Overweight")
    else:
        print("Obese")
else:
    print(result)
