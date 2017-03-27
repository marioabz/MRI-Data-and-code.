# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 14:37:15 2017

@author: Mario
"""

from tkinter import Tk, geometry, DoubleVar, destroy, quit, Button, Scale, title

def finish():
    a,b= v1.get(),v2.get()
    master.destroy()
    master.quit()
    return a,b
    
    

master = Tk()
master.geometry("400x300")
v1,v2=DoubleVar(),DoubleVar()
master.title("Choose values between 0-1 to perform contrast stretching ")

w = Scale(master, label='First value', orient=HORIZONTAL, from_=0.0, to=1.0,
          length=200, resolution=0.01, variable=v1).place(x=100,y=20)

z = Scale(master, label='Second value', orient=HORIZONTAL, from_=0.0, to=1.0,
          length=200, resolution=0.01, variable=v2).place(x=100,y=90)

b1= Button(master, text="Save values",command= finish).place(x=160, y=200)

master.mainloop()






