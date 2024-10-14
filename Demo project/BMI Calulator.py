def calculate_bmi(weight, height):
    """
    Function to calculate BMI (Body Mass Index)
    Formula: BMI = weight (kg) / (height (m) ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Function to interpret BMI value and provide a category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def convert_to_meters(feet, inches):
    """
    Function to convert height from feet and inches to meters
    1 foot = 0.3048 meters
    1 inch = 0.0254 meters
    """
    total_inches = feet * 12 + inches
    meters = total_inches * 0.0254
    return meters

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    feet = int(input("Enter your height in feet: "))
    inches = int(input("Enter the remaining inches: "))

    height = convert_to_meters(feet, inches)
    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print("Interpretation:", category)

if __name__ == "__main__":
    main()
