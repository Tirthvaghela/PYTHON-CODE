#from Tkinter import *
#import Tkinter
from tkinter import *
import tkinter
from tkinter import messagebox

def show_entry_fields():
	print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
def del1():
	e1.delete(0,END)
	e2.delete(0,END)

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.insert(0,"GLS")
e2.insert(0,"University")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1)
Button(master, text='Delete', command=del1).grid(row=3, column=2)


mainloop( )
