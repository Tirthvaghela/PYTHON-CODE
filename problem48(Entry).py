import tkinter as tk
from tkinter import messagebox

def submit():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()

    if not first_name or not last_name:
        messagebox.showwarning("Input Error", "Please enter both first and last names!")
    else:
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")

root = tk.Tk()
root.title("Name Entry Form")
root.geometry("300x200")

label_first_name = tk.Label(root, text="First Name:")
label_first_name.pack(pady=5)
entry_first_name = tk.Entry(root)
entry_first_name.pack(pady=5)

label_last_name = tk.Label(root, text="Last Name:")
label_last_name.pack(pady=5)
entry_last_name = tk.Entry(root)
entry_last_name.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

root.mainloop()
