from tkinter import *
from tkinter import ttk

root = Tk()

button1 = ttk.Button(root,text = 'Button 1')
button1.pack()

button2 = ttk.Button(root,text = 'Button 2')
button2.pack()

button3 = ttk.Button(root,text = 'Button 3')
button3.pack()

style = ttk.Style()
style.theme_names()

style.theme_use()

style.theme_use('classic')
style.configure('TButton',foreground ='red')

button1.winfo_class()


style.configure('TButton',foreground ='red',font=('Arial',24))
style.configure('Info.TButton',foreground = 'blue',font=('Arial',18,'bold'))

button3.configure(style = 'Info.TButton')

style.map('Info.TButton',background=[('pressed','blue'),('disabled','grey')])

#button3.state(['disabled'])
