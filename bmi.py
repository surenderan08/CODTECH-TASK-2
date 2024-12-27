import tkinter as tk
from tkinter import messagebox
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("300x200")  # Set window size
tk.Label(app, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(app)
weight_entry.pack()

tk.Label(app, text="Height (cm):").pack(pady=5)
height_entry = tk.Entry(app)
height_entry.pack()
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        messagebox.showinfo("BMI Result", f"BMI: {bmi:.1f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

tk.Button(app, text="Calculate BMI", command=calculate_bmi).pack(pady=20)
app.configure(bg="lightblue")
tk.Label(app, text="BMI Calculator", font=("Arial", 16), bg="lightblue").pack(pady=10)
def clear_inputs():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

tk.Button(app, text="Clear", command=clear_inputs).pack(pady=10)

