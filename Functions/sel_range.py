# -*- coding: utf-8 -*-
"""
@author: Mario
"""

from tkinter import *
import tkinter as tk

master = Tk()

def get_range(master):
    
    def show_values():
        global a,b
        a,b=w1.get(),w2.get()
        master.destroy()
        master.quit()

    master.title("Choose image range intensities")
    master.geometry("400x200")
    w1 = Scale(master, label= "Valor 1", from_=0, to=1, orient= HORIZONTAL, resolution= 0.01,
               length=200)
    w1.pack()
    w2 = Scale(master, label= "Valor 2", from_=0, to=1, orient= HORIZONTAL, resolution= 0.01,
               length=200)
    w2.pack()
    Button(master, text='Save', command=show_values).pack()
    
    tk.mainloop()
    return (a,b)


#f=get_range(master)






