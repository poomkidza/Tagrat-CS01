from tkinter import *
root = Tk()
root.title("First GUI")
myText = Label(text="My name Tag ",fg="pink",font=20).grid(row=0,column=0)
myText = Label(text="Tangrat ",fg="pink",font=20).grid(row=1,column=1)
myText = Label(text="Kantama ",fg="yellow",font=20).grid(row=2,column=2)
root.mainloop()