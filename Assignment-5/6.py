import tkinter as tk
from tkinter import messagebox

def on_button_click(color):
    messagebox.showinfo("Button Clicked", f"You clicked the {color} button!")

root = tk.Tk()
root.title("Colored Buttons")

colors = ["Red", "Yellow", "Green", "Blue", "Orange", "Purple", "Pink"]
color_values = ["red", "yellow", "green", "blue", "orange", "purple", "pink"]

for i in range(len(colors)):
    button = tk.Button(root, text=colors[i], bg=color_values[i], fg="white", 
                       command=lambda c=colors[i]: on_button_click(c))
    button.pack(pady=5, padx=10, fill='x')

root.mainloop()