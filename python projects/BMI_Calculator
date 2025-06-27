import tkinter as tk
from tkinter import ttk, messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        unit = height_unit.get()

        if unit == "cm":
            height_m = height / 100
        elif unit == "feet":
            height_m = height * 0.3048
        else:
            messagebox.showerror("Error", "Please select a height unit.")
            return

        bmi = weight / (height_m ** 2)
        bmi_rounded = round(bmi, 2)
        bmi_label.config(text=f"BMI: {bmi_rounded}")

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Healthy"
        elif 24.9 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Suffering from Obesity"

        category_label.config(text=f"Category: {category}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values for height and weight.")

root = tk.Tk()
root.title("BMI Calculator")

height_label = ttk.Label(root, text="Enter your height:")
height_label.grid(column=0, row=0, padx=10, pady=10, sticky='W')

height_entry = ttk.Entry(root)
height_entry.grid(column=1, row=0, padx=10, pady=10)

height_unit = tk.StringVar(value="cm")

cm_radio = ttk.Radiobutton(root, text="Centimeters (cm)", variable=height_unit, value="cm")
cm_radio.grid(column=0, row=1, padx=10, sticky='W')

feet_radio = ttk.Radiobutton(root, text="Feet (ft)", variable=height_unit, value="feet")
feet_radio.grid(column=1, row=1, padx=10, sticky='W')

weight_label = ttk.Label(root, text="Enter your weight (kg):")
weight_label.grid(column=0, row=2, padx=10, pady=10, sticky='W')

weight_entry = ttk.Entry(root)
weight_entry.grid(column=1, row=2, padx=10, pady=10)

calc_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(column=0, row=3, columnspan=2, pady=15)

bmi_label = ttk.Label(root, text="BMI: ")
bmi_label.grid(column=0, row=4, columnspan=2, pady=5)

category_label = ttk.Label(root, text="Category: ")
category_label.grid(column=0, row=5, columnspan=2, pady=5)

root.mainloop()
