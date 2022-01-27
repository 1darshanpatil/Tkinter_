from tkinter import *
from sympy import isprime
from tkinter import ttk
root = Tk()
Info = Label(root, text = 'Enter any integer to check if it is prime or not')
Info.pack()
e = Entry(root, width = 50)
e.pack()

def button1():
    entry = int(e.get())
    if isprime(entry):
        S = f'{entry} is a prime number.'
    else:
        S = f'{entry} is not a prime number'
        
    mylabel = Label(root, text = str(S))
    mylabel.pack()
mybutton1 = Button(root, text = 'Check', command = button1)
mybutton1.pack()
root.mainloop()
