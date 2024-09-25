import tkinter
from tkinter import messagebox

def heloo(): 
    messagebox.showinfo("hello guys", "hello broo")

Window = tkinter.Tk()
Window.geometry("300x300") 

btn = tkinter.Button(Window, text="ok", command=heloo) 
btn.pack()

Window.mainloop()