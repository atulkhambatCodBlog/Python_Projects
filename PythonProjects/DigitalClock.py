from cProfile import label
from cgitb import text
import string
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from time import strftime
from webbrowser import BackgroundBrowser

root= Tk()
root.title("Clock")
def time():
    string=string('%H:%M:%S %P')
    label.config(text=string)
    label.after(1000,time)

label=label(root)
label.pack(anchor="center")
time()
mainloop()