from tkinter import *
from tkinter import ttk

root = Tk()


entry = ttk.Entry(root, width = 30)
entry.pack()
button = ttk.Button(root,text ="Click Me")
button.pack()

def BuClick():
    print(entry.get())
    entry.delete(0,END)
button.config(command = BuClick)
root.mainloop()

