from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from subprocess import call

root = Tk()

def login():
    username = users.get()
    password = pas.get()

    if not username and not password:
        messagebox.showerror("Error", "Data missing. Please enter username and password.")
    elif  not username :
        messagebox.showerror("Error", "Data missing. Please enter username .")
    elif  not password:
        messagebox.showerror("Error", "Data missing. Please enter  password.")
    elif username == "p" and password == "p":
        root.destroy()
        call(["python", "home.py"])
    else:
        messagebox.showerror("Error", "Incorrect username or password.")

def cancel():
    root.destroy()

root.title(" Login Page ")

jpg_image = Image.open("C:/Users/jassi/OneDrive/Desktop/OCAC/img/log.jpg")
image = ImageTk.PhotoImage(jpg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight())))

background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
font = ("Helvetica", 15)

border = LabelFrame(root, text="Login", bg="cadetblue", bd=10, fg="maroon", font=("arial", 25))
border.pack(fill="both", expand="yes", padx=350, pady=150)

Label(border, text="Username : ", font=("comicsansms", 20), bg="cadetblue").place(x=50, y=80)
users = Entry(border, bg="grey", font=font, bd=5)
users.place(x=250, y=80)

Label(border, text="Password : ", font=("comicsansms", 20), bg="cadetblue").place(x=50, y=130)
pas = Entry(border, show="*", bg="grey", font=font, bd=5)
pas.place(x=250, y=130)

Button(border, text="Submit", command=login, height=1, width=10, bg="lawngreen", font=10).place(x=200, y=230)
Button(border, text="Exit", command=cancel, height=1, width=10, bg="chocolate", font=10).place(x=400, y=230)

root.mainloop()
