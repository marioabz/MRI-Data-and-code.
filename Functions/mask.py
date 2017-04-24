# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:04:33 2017

@author: Mario
"""

import numpy as np
from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


def select_threshold_mask(X):
    
    def on_key_event(event):
       print('you pressed %s'%event.key)
       key_press_handler(event, canvas, toolbar)

    def _quit():
        ui.quit()    
        ui.destroy() 
       
    def open_w():
       global a
       global canvas1
           
       var = IntVar()
       f = Figure(figsize=(5,4),dpi=100)
       a = f.add_subplot(111)
       a.imshow(X)
       canvas1 = FigureCanvasTkAgg(f,master = ui)
       canvas1.show()
       canvas1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
       toolbar = NavigationToolbar2TkAgg(canvas1, ui )
       toolbar.update()
       canvas1._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
       slider = Scale(ui,orient=HORIZONTAL,length = 300,from_=X.min(),to=X.max(),variable=var,command=_update)
       slider.pack()
       button = Button(master=ui, text='Quit', command=_quit)
       button.pack(side = BOTTOM)
       canvas1.mpl_connect('key_press_event', on_key_event)
   
    def _update(var):
       global z
       z=int(float(var))
       Y= X>z
       a.imshow(Y,cmap='gray')
       canvas1.show()
       return z

    ui = Tk()
    open_w()
    ui.title('Area where histogram equalization is performed')
    ui.mainloop()
    
    return z
#