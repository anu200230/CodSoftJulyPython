import string
import random
from tkinter import *

characters = string.printable


def generate():
    password_length = int(entry2.get())
    password = ""

    for _ in range(password_length):
        password += random.choice(characters)

    entry3.config(state="normal")
    entry3.delete(0, END)
    entry3.insert(0, password)
    entry3.config(state="readonly")


def reset():
    entry3.config(state="normal")
    entry3.delete(0, END)
    entry3.config(state="readonly")


def accept():
    text = entry3.get()
    if text:
        exit()


root = Tk()
root.geometry("800x700")
root.title("Password Generator")
canvas = Canvas(root, width=800, height=700, bg="#3E001F")
canvas.create_text(400, 70, text="Password Generator",
                   fill="white", font=("Bold", 40))

canvas.create_rectangle(80, 120, 700, 450, fill="#FFE5AD")

label1 = Label(canvas, text="Enter Username :", font=("Times New Roman", 15),bg="#F11A7B",fg="white")
label1.place(x=120, y=220)
entry1 = Entry(canvas, font=("Times New Roman", 15), width=33, border=3)
entry1.place(x=300, y=220)

label2 = Label(canvas, text="Password Length :", font=("Times New Roman", 15),bg="#F11A7B",fg="white")
label2.place(x=120, y=280)
entry2 = Entry(canvas, font=("Times New Roman", 15), width=33, border=3)
entry2.place(x=300, y=280)

label3 = Label(canvas, text="Generated\n Password :", font=("Times New Roman", 15),bg="#F11A7B",fg="white")
label3.place(x=120, y=360)
entry3 = Entry(canvas, font=("Times New Roman", 15), width=33, border=3)
entry3.place(x=300, y=370)
entry3.config(state="readonly")


# BUTTONS IN GUI
button_1 = Button(canvas, text='Generate', height=2, width=10, bg="#982176",
                  fg="white", font=("Times New Roman", 15), borderwidth=3, command=generate)
button_1.place(x=150, y=500)

button_2 = Button(canvas, text='Accept', height=1, width=10,
                  bg="#F11A7B", fg="white", font=("Times New Roman", 15), borderwidth=3, command=accept)
button_2.place(x=350, y=510)

button_3 = Button(canvas, text='Reset', height=1, width=10,
                  bg="#F11A7B", fg="white", font=("Times New Roman", 15), borderwidth=3, command=reset)
button_3.place(x=500, y=510)

canvas.pack()


root.mainloop()