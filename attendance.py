import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from subprocess import call

def calculate_attendance():
    try:
        attendance = [int(var.get()) for var in attendance_vars]

        total_attendance = sum(attendance)
        total_days = len(attendance)
        attendance_percentage = (total_attendance / total_days) * 100

        result_label.config(text=f"Attendance Percentage: {attendance_percentage:.2f}%")

    except ValueError:
        messagebox.showerror("Error", "Please select attendance for all 15 days.")

def home():
    root.destroy()
    call(["python", "home.py"])

root = tk.Tk()
root.title("Attendance Calculator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

jpg_image = Image.open("C:/Users/jassi/OneDrive/Desktop/OCAC/img/att.jpg")
image = ImageTk.PhotoImage(jpg_image.resize((screen_width, screen_height)))

background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_frame = tk.Frame(root,bg="bisque")
title_frame.pack(fill="both")

title_label = tk.Label(title_frame, text="ATTENDANCE CALCULATOR", font=("Helvetica", 12), fg="black", bg="bisque")
title_label.pack(pady=5)

border_frame = tk.Frame(root, borderwidth=2, bd=1, relief="ridge", padx=20, pady=1, bg="lightblue")
border_frame.pack()

attendance_vars = []
for i in range(1, 16):
    day_label = tk.Label(border_frame, text=f"Day {i}:", bg="lightblue")
    day_label.grid(row=i, column=0, padx=10, pady=5)

    var = tk.IntVar()
    attendance_vars.append(var)

    present_radio = tk.Radiobutton(border_frame, text="Present", variable=var, value=1, bg="lightblue")
    absent_radio = tk.Radiobutton(border_frame, text="Absent", variable=var, value=0, bg="lightblue")

    present_radio.grid(row=i, column=1, padx=5, pady=5)
    absent_radio.grid(row=i, column=2, padx=5, pady=5)

calculate_button = tk.Button(border_frame, text="Calculate", command=calculate_attendance, bg="khaki")
calculate_button.grid(row=16, column=0, columnspan=3, pady=10)

result_label = tk.Label(border_frame, text="", bg="lightblue")
result_label.grid(row=17, column=0, columnspan=3)
back_button = tk.Button(root, text="Back", command=home, height=1, width=10, bg="springgreen", font=("Helvetica", 10))
back_button.place(x=130, y=550)
root.geometry(f"{screen_width}x{screen_height}")

root.mainloop()
