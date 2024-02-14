import tkinter as tk
from tkinter import ttk, messagebox
from subprocess import call
from PIL import Image, ImageTk


def is_valid_input(entry):
    value = entry.get()
    if not value:
        return None
    try:
        float_value = float(value)
        if float_value < 0:
            return "negative"
        return float_value
    except ValueError:
        return "invalid"

def calculate_balance():
    valid_income_entries = []
    valid_expense_entries = []

    for i in range(7):
        income_entry = income_entries[i]
        expense_entry = expense_entries[i]

        income_result = is_valid_input(income_entry)
        expense_result = is_valid_input(expense_entry)

        if income_result is None and expense_result is None:
            messagebox.showerror("Error", f"Enter the values")
            return
        if not income_result  and not expense_result :
            messagebox.showerror("Error", f"Enter valid income and expense value for Day {days[i]}")
            return
        if not income_result  :
            messagebox.showerror("Error", f"Enter valid income value for Day {days[i]}")
            return
        if  not expense_result :
            messagebox.showerror("Error", f"Enter valid expense value for Day {days[i]}")
            return
        if income_result == "negative" or expense_result == "negative":
            messagebox.showerror("Error", f"Value cannot be negative for Day {days[i]}")
            return
        if income_result == "non-numeric" or expense_result == "non-numeric":
            messagebox.showerror("Error", f"Enter a positive numeric value for Day {days[i]}.")
            return
        if income_result == "negative" or expense_result == "negative":
            messagebox.showerror("Error", "enter a positive value")
            return
        if income_result is not None:
            valid_income_entries.append(income_result)

        if expense_result is not None:
            valid_expense_entries.append(expense_result)

    if not valid_income_entries and not valid_expense_entries:
        messagebox.showinfo("Info", "Please enter income/expense values.")
    else:
        total_income = sum(valid_income_entries)
        total_expenses = sum(valid_expense_entries)
        balance.set(total_income - total_expenses)


def home():
    root.destroy()
    call(["python", "home.py"])


root = tk.Tk()
root.title("Income Expense Calculator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

jpg_image = Image.open("C:/Users/jassi/OneDrive/Desktop/OCAC/img/in.jpg")
image = ImageTk.PhotoImage(jpg_image.resize((screen_width, screen_height)))

background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_frame = tk.Frame(root, bg="antiquewhite")
label_frame.pack(side="top", fill="x")

title_label = tk.Label(label_frame, text=" INCOME AND EXPENSE CALCULATOR ", font=("Helvetica", 25), fg="crimson",
                       bg="antiquewhite")
title_label.pack(pady=10)

border = tk.Frame(root, relief="ridge", borderwidth=2, bg="powderblue", bd=3)
border.pack(padx=20, pady=20)

income_heading_label = tk.Label(border, text="Income", font=("Helvetica", 16), bg="powderblue")
income_heading_label.grid(row=0, column=1, padx=5, pady=5)

expense_heading_label = tk.Label(border, text="Expense", font=("Helvetica", 16), bg="powderblue")
expense_heading_label.grid(row=0, column=3, padx=5, pady=5)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_labels = []

for i in range(7):
    day_label = tk.Label(border, text=days[i], bg="powderblue")
    day_label.grid(row=i + 1, column=0, padx=5, pady=5)
    day_labels.append(day_label)

income_entries = []
expense_entries = []

for i in range(7):
    income_entry = tk.Entry(border)
    income_entry.grid(row=i + 1, column=1, padx=5, pady=5)
    income_entries.append(income_entry)

    expense_entry = tk.Entry(border)
    expense_entry.grid(row=i + 1, column=3, padx=5, pady=5)
    expense_entries.append(expense_entry)

calculate_button = tk.Button(border, text="Calculate Balance", command=calculate_balance, bg="lightcoral")
calculate_button.grid(row=8, column=0, columnspan=4, padx=5, pady=10)

balance = tk.StringVar()
balance_label = tk.Label(border, text="Balance:", bg="powderblue")
balance_label.grid(row=9, column=0, padx=5, pady=5)
balance_display = tk.Label(border, textvariable=balance, bg="powderblue")
balance_display.grid(row=9, column=1, padx=5, pady=5)

back_button = tk.Button(root, text="Back", command=home, height=1, width=10, bg="springgreen", font=("Helvetica", 10))
back_button.place(x=130, y=580)

root.geometry(f"{screen_width}x{screen_height}")
root.mainloop()
