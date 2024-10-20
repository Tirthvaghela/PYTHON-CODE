import tkinter
from tkinter import *

lang=[("Python"),("C"),("C++"),("Java")]

root=Tk()
root.geometry("400x400")

def show():
    choice=v.get()
    print(choice)
    if choice==0:
        print("Python")
    elif choice==1:
        print("C")
    elif choice==2:
        print("C++")
    elif choice==3:
        print("Java")
    else:
        print("Invalid")


lbl=Label(root, text="""Choose Your fav Language""",justify=LEFT)
lbl.pack()
v=IntVar()
for val,lang in enumerate(lang):
    r1=Radiobutton(root,text=lang,padx=10,variable=v,command=show,value=val)
    r1.pack()

root.mainloop()