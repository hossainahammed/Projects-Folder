import tkinter as tk


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


def calculate_button_clicked():
    weight = float(weight_entry.get())
    feet = int(feet_entry.get())
    inches = int(inches_entry.get())

    height = convert_to_meters(feet, inches)
    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    result_label.config(text=f"Your BMI is: {bmi:.2f}\nInterpretation: {category}")


# GUI setup
root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Height:")
height_label.grid(row=1, column=0)

feet_entry = tk.Entry(root, width=5)
feet_entry.grid(row=1, column=1)

feet_label = tk.Label(root, text="feet")
feet_label.grid(row=1, column=2)

inches_entry = tk.Entry(root, width=5)
inches_entry.grid(row=1, column=3)

inches_label = tk.Label(root, text="inches")
inches_label.grid(row=1, column=4)

calculate_button = tk.Button(root, text="Calculate", command=calculate_button_clicked)
calculate_button.grid(row=2, column=0, columnspan=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=5)

root.mainloop()
