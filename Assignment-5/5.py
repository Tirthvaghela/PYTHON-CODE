import tkinter as tk

def update_label():
    label.config(text="Selected: None")  

def show_selection():
    label.config(text="Selected: " + gender_var.get())

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Gender Selection")

gender_var = tk.StringVar(value="")

label = tk.Label(root, text="Selected: None")
label.pack()

radiobutton_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", command=update_label)
radiobutton_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", command=update_label)

radiobutton_male.pack(anchor='w')
radiobutton_female.pack(anchor='w')

submit_button = tk.Button(root, text="Submit", command=show_selection)
submit_button.pack()

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack()

root.mainloop()