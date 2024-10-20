import tkinter 
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Hello! You clicked the button.")

root= tkinter.Tk()
root.geometry("300x300")

button=tkinter.Button(root , text="Click me", command=show_message)

button.pack(pady=20)

root.mainloop()