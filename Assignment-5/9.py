import tkinter as tk

def on_select(event):
    selected_language = listbox.get(listbox.curselection())
    label.config(text=f"Selected Language: {selected_language}")

root = tk.Tk()
root.title("Programming Languages")

languages = ["Python", "C", "C++", "Java", "React"]
listbox = tk.Listbox(root, height=5, selectmode=tk.SINGLE)

for language in languages:
    listbox.insert(tk.END, language)

listbox.pack(pady=10)
listbox.bind('<<ListboxSelect>>', on_select)

label = tk.Label(root, text="Selected Language: None")
label.pack(pady=10)

root.mainloop()
