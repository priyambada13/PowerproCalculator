import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from subprocess import call

def is_positive_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def convert_temperature():
    temp_input = entry_temp.get()
    if not temp_input:
        messagebox.showerror("Error", "Please enter a temperature value.")
    elif not is_positive_float(temp_input):
        messagebox.showerror("Error", "Please enter a valid positive number for temperature.")
    elif float(temp_input) < 0:
        messagebox.showerror("Error", "Temperature value cannot be negative.")
    else:
        celsius = float(temp_input)
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius} °C = {fahrenheit:.2f} °F")

def convert_length():
    length_input = entry_length.get()
    if not length_input:
        messagebox.showerror("Error", "Please enter a length value.")
    elif not is_positive_float(length_input):
        messagebox.showerror("Error", "Please enter a valid positive number for length.")
    elif float(length_input) < 0:
        messagebox.showerror("Error", "Length value cannot be negative.")
    else:
        length = float(length_input)
        if length_type.get() == 1:  # Meters to Kilometers
            kilometers = length / 1000
            result_label.config(text=f"{length} meters = {kilometers:.2f} km")
        elif length_type.get() == 2:  # Kilometers to Meters
            meters = length * 1000
            result_label.config(text=f"{length} km = {meters:.2f} meters")
        elif length_type.get() == 3:  # Centimeters to Meters
            meters = length / 100
            result_label.config(text=f"{length} cm = {meters:.2f} meters")
        elif length_type.get() == 4:  # Meters to Centimeters
            centimeters = length * 100
            result_label.config(text=f"{length} meters = {centimeters:.2f} cm")

def home():
    root.destroy()
    call(["python", "home.py"])
root = tk.Tk()
root.title("Converter Calculator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

jpg_image = Image.open("C:/Users/jassi/OneDrive/Desktop/OCAC/img/con.jpg")
image = ImageTk.PhotoImage(jpg_image.resize((screen_width, screen_height)))

background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_frame = tk.Frame(root, bg="antiquewhite")
title_frame.pack(fill="both")

title_label = tk.Label(title_frame, text="CONVERTER CALCULATOR", font=("Helvetica", 25), fg="crimson", bg="antiquewhite")
title_label.pack(pady=10)

border_frame = tk.Frame(root, padx=10, pady=10, relief=tk.SUNKEN, borderwidth=2, bg="linen")
border_frame.pack()

temp_label = tk.Label(border_frame, text="Enter Temperature (°C):", font=("comicsansms", 25), bg="linen")
temp_label.pack(pady=5)

entry_temp = tk.Entry(border_frame, font=("Helvetica", 15))
entry_temp.pack(pady=5)

convert_temp_button = tk.Button(border_frame, text="Convert", command=convert_temperature, font=10, bg="lightcoral")
convert_temp_button.pack(pady=5)

length_label = tk.Label(border_frame, text="Enter Length:", font=("comicsansms", 25), bg="linen")
length_label.pack(pady=5)

entry_length = tk.Entry(border_frame, font=("Helvetica", 15))
entry_length.pack(pady=5)

length_type = tk.IntVar()
length_type.set(1)

radio_meter_to_km = tk.Radiobutton(border_frame, font=("comicsansms", 15), text="Meters to Kilometers", variable=length_type, value=1, bg="linen")
radio_km_to_meter = tk.Radiobutton(border_frame, font=("comicsansms", 15), text="Kilometers to Meters", variable=length_type, value=2, bg="linen")
radio_cm_to_meter = tk.Radiobutton(border_frame, font=("comicsansms", 15), text="Centimeters to Meters", variable=length_type, value=3, bg="linen")
radio_meter_to_cm = tk.Radiobutton(border_frame, font=("comicsansms", 15), text="Meters to Centimeters", variable=length_type, value=4, bg="linen")

radio_meter_to_km.pack(pady=5)
radio_km_to_meter.pack(pady=5)
radio_cm_to_meter.pack(pady=5)
radio_meter_to_cm.pack(pady=5)

convert_length_button = tk.Button(border_frame, text="Convert Length", command=convert_length, font=10, bg="lightcoral")
convert_length_button.pack(pady=5)

result_label = tk.Label(border_frame, text="", font=("Helvetica", 14), bg="linen")
result_label.pack()
back_button = tk.Button(root, text="Back", command=home, height=1, width=10, bg="springgreen", font=("Helvetica", 10))
back_button.place(x=130, y=550)
root.geometry(f"{screen_width}x{screen_height}")

root.mainloop()
