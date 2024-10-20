import tkinter as tk

def update_label():
    selected_values = []
    for i in range(len(variables)):
        if variables[i].get() == 1:
            selected_values.append(checkbutton_texts[i])
    label.config(text="Selected: " + ", ".join(selected_values))

root = tk.Tk()
root.title("Checkbutton Example")

checkbutton_texts = ["BANANA", "CHIKEN", "APPLE"]
variables = []

for text in checkbutton_texts:
    var = tk.IntVar()
    variables.append(var)
    checkbutton = tk.Checkbutton(root, text=text, variable=var, command=update_label)
    checkbutton.pack(anchor='w')

label = tk.Label(root, text="Selected: None")
label.pack()

root.mainloop()
