import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        total = num1 + num2
        messagebox.showinfo("Sum", f"The sum is: {total}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Sum of Two Numbers")

label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

button = tk.Button(root, text="Calculate Sum", command=calculate_sum)
button.pack(pady=10)

root.mainloop()