from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ActivePlayer = 1
p1 =[]
p2=[]
root = Tk()
root.title("Tic Tac: player 1")
# Add Buttons
b1 = ttk.Button(root,text=' ')
b1.grid(row = 0,column = 0,sticky='snew',ipadx = 40,ipady = 40)
b1.config(command= lambda: ButtonClick(1))

b2 = ttk.Button(root,text=' ')
b2.grid(row = 0,column = 1,sticky='snew',ipadx = 40,ipady = 40)
b2.config(command= lambda: ButtonClick(2))


b3 = ttk.Button(root,text=' ')
b3.grid(row = 0,column = 2,sticky='snew',ipadx = 40,ipady = 40)
b3.config(command= lambda: ButtonClick(3))

b4 = ttk.Button(root,text=' ')
b4.grid(row = 1,column = 0,sticky='snew',ipadx = 40,ipady = 40)
b4.config(command= lambda: ButtonClick(4))

b5 = ttk.Button(root,text=' ')
b5.grid(row = 1,column = 1,sticky='snew',ipadx = 40,ipady = 40)
b5.config(command= lambda: ButtonClick(5))

b6 = ttk.Button(root,text=' ')
b6.grid(row = 1,column = 2,sticky='snew',ipadx = 40,ipady = 40)
b6.config(command= lambda: ButtonClick(6))



b7 = ttk.Button(root,text=' ')
b7.grid(row = 2,column = 0,sticky='snew',ipadx = 40,ipady = 40)
b7.config(command= lambda: ButtonClick(7))


b8 = ttk.Button(root,text=' ')
b8.grid(row = 2,column = 1,sticky='snew',ipadx = 40,ipady = 40)
b8.config(command= lambda: ButtonClick(8))



b9 = ttk.Button(root,text=' ')
b9.grid(row = 2,column = 2,sticky='snew',ipadx = 40,ipady = 40)
b9.config(command= lambda: ButtonClick(9 ))

def ButtonClick(id):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id,"X")
        p1.append(id)
        root.title("Tic tac toy : Player 2")
        ActivePlayer = 2
        print("P1:{}".format(p1))
    elif(ActivePlayer==2):
        SetLayout(id,"0")
        p2.append(id)
        root.title("Tic tac toy : Player 1")
        ActivePlayer =1
        print("P2:{}".format(p2))


def SetLayout(id,PlayerSymbol):
    if id==1:
        b1.config(text = PlayerSymbol)
        b1.state(['disabled'])
    elif id==2:
        b2.config(text = PlayerSymbol)
        b2.state(['disabled']) 

    elif id==3:
        b3.config(text = PlayerSymbol)
        b3.state(['disabled'])

    elif id==4:
        b4.config(text = PlayerSymbol)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text = PlayerSymbol)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text = PlayerSymbol)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text = PlayerSymbol)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text = PlayerSymbol)
        b8.state(['disabled'])
    elif id==9:
        b9.config(text = PlayerSymbol)
        b9.state(['disabled'])




        




root .mainloop()
