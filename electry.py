import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from subprocess import call

def calculate_total_amount():
    try:
        units_consumed = float(entry_units_consumed.get())
        if units_consumed < 0:
            messagebox.showerror("Invalid Input", "Units consumed cannot be negative.")
        else:
            rate_per_unit = 7.5
            total_amount = units_consumed * rate_per_unit
            result_label.config(text=f"Total Amount: ₹{total_amount:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")

def home():
    root.destroy()
    call(["python", "home.py"])

root = tk.Tk()
root.title("Electricity Calculator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

jpg_image = Image.open("C:/Users/jassi/Downloads/elec.jpg")
image = ImageTk.PhotoImage(jpg_image.resize((screen_width, screen_height)))

background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(root, text="ELECTRICITY CALCULATOR", font=("Helvetica", 25), fg="crimson", bg="antiquewhite")
title_label.pack(pady=30)

border_frame = tk.Frame(root, borderwidth=2, relief="ridge", bg="lightskyblue", bd=10)
border_frame.pack(padx=20, pady=20)

units_label = tk.Label(border_frame, text="Enter Units Consumed:", font=("comicsansms", 25), bg="lightskyblue")
units_label.pack(pady=20, padx=10)

entry_units_consumed = tk.Entry(border_frame, bd=5, bg="grey")
entry_units_consumed.pack(pady=10, padx=10)

calculate_button = tk.Button(border_frame, text="Calculate", command=calculate_total_amount, bg="peru")
calculate_button.pack(pady=10)

result_label = tk.Label(border_frame, text="", font=("Helvetica", 14), bg="lightskyblue")
result_label.pack(pady=10)

back_button = tk.Button(root, text="Back", command=home, height=1, width=10, bg="springgreen", font=("Helvetica", 10))
back_button.place(x=130, y=550)

root.geometry(f"{screen_width}x{screen_height}")

root.mainloop()
