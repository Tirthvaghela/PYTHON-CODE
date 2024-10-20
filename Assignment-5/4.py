import tkinter as tk

def update_message():
    if age_var.get() == "less":
        message = "You are not eligible for voting."
    else:
        message = "You are eligible for voting."
    label.config(text=message)

root = tk.Tk()
root.title("Voting Eligibility")

age_var = tk.StringVar(value="less")

label = tk.Label(root, text="")
label.pack()

radiobutton_less = tk.Radiobutton(root, text="Less than 18", variable=age_var, value="less", command=update_message)
radiobutton_greater = tk.Radiobutton(root, text="Greater than 18", variable=age_var, value="greater", command=update_message)

radiobutton_less.pack(anchor='w')
radiobutton_greater.pack(anchor='w')

root.mainloop()
