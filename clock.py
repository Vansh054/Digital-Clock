from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
label = Label(root, font=('algerian',40),background="black",foreground="white")
label.pack(anchor='center')

def fetchtime() :
    t = strftime("%H : %M : %S : %p")
    label.config(text=t)
    label.after(1000,fetchtime)


fetchtime()

root.mainloop()
