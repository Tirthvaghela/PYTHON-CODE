import tkinter as tk
from tkinter import messagebox

def submit_form():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    designation = entry_designation.get()
    company = entry_company.get()
    country = entry_country.get()
    
    info = f"First Name: {first_name}\nLast Name: {last_name}\ndesignation: {designation}\nCompany: {company}\nCountry: {country}"
    messagebox.showinfo("Submitted Information", info)

root = tk.Tk()
root.geometry("400x400")
root.title("User Information Form")

# Create labels and entry fields
label_first_name = tk.Label(root, text="First Name:")
label_first_name.pack(pady=5)
entry_first_name = tk.Entry(root)
entry_first_name.pack(pady=5)

label_last_name = tk.Label(root, text="Last Name:")
label_last_name.pack(pady=5)
entry_last_name = tk.Entry(root)
entry_last_name.pack(pady=5)

label_designation = tk.Label(root, text="designation:")
label_designation.pack(pady=5)
entry_designation = tk.Entry(root)
entry_designation.pack(pady=5)

label_company = tk.Label(root, text="Company:")
label_company.pack(pady=5)
entry_company = tk.Entry(root)
entry_company.pack(pady=5)

label_country = tk.Label(root, text="Country:")
label_country.pack(pady=5)
entry_country = tk.Entry(root)
entry_country.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=10)

root.mainloop()
