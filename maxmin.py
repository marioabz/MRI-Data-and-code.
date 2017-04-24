# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 00:17:32 2017

@author: Mario
"""
import os,dicom
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np

os.listdir()

folder=filedialog.askdirectory()

list=os.listdir(folder)
x=[]


b=os.listdir(folder)
for i in b:
        data=dicom.read_file(folder+'/'+i)
        x.append(data.pixel_array)

plt.hist(x[0].ravel(),bins=200)
plt.hist(x[1].ravel(),bins=200)
plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        