from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from subprocess import call
root=Tk()
jpg_image = Image.open("C:/Users/jassi/OneDrive/Desktop/OCAC/img/background.jpg")
image = ImageTk.PhotoImage(jpg_image)
background_label = tk.Label(root,image=image)
background_label.place(relwidth=1, relheight=1)
def myincome():
    root.destroy()
    call(["python", "income.py"])

def convert():
    root.destroy()
    call(["python", "convert.py"])

def attendance():
    root.destroy()
    call(["python","attendance.py"])
def electry():
    root.destroy()
    call(["python", "electry.py"])

def home():
    root.destroy()
    call(["python", "login.py"])
root.title(" Home Page ")
Label(root,text=" Welcome to Powerpro Calculator ",font=("comicsansms",50),fg="Brown",bg="lavender").pack(pady=50)
income_button = Button(root, text="Income & Expense Calculation",command=myincome, font=50,bg="burlywood",width=25)
income_button.pack(pady=30)
converter_button = Button(root, text="Converter",command=convert,font=50,bg="burlywood",width=25)
converter_button.pack(pady=30)
attendance_button = Button(root, text="Attendance Calculation",command=attendance,font=50,bg="burlywood",width=25)
attendance_button.pack(pady=30)

electricity_button = Button(root, text="Electricity Calculation",command=electry,font=50,bg="burlywood",width=25)
electricity_button.pack(pady=30)

Button(root,text="Back",command=home,height=1,width=10,bg="springgreen",font=10).place(x=160,y=580)
root.configure(background="teal")
root.geometry("1600x800")
root.mainloop()