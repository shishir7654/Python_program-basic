from tkinter import *
from tkinter import ttk
root =Tk()
button = ttk.Button(root,text = "Click me")
button.pack()


def BuClick():
    print("Button is clicked")

button.config(command = BuClick)

button.invoke()
