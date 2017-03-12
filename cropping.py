@author: Mario

from matplotlib.pyplot import draw,ion
import matplotlib.pyplot as plt
import dicom
import numpy as np
import tkinter as tk
from tkinter import filedialog

def scale(X):
    A=np.array(X)
    mx=np.amax(X)
    mn=np.amin(X)
    A=(X-mn)/(mx-mn)
    return np.float32(A)

axes = np.zeros((2, 2), dtype=np.object)
root = tk.Tk()
root.withdraw()
folder= filedialog.askopenfilenames()

ls=[]
for x in folder:
    ls.append(dicom.read_file(x).pixel_array)

ion()
fig = plt.figure()
axes[0,0]=fig.add_subplot(1,2,1)
axes[1,0]=fig.add_subplot(1,2,2)
axes[0,0].imshow(ls[0],cmap='gray')
axes[1,0].imshow(ls[1],cmap='gray')



input('Click enter...')

for i in range(len(folder)):
    x0=int(input('Punto x de primera esquina: '))
    y0=int(input('Punto y de primera esquina: '))
    xf=int(input('Punto x de contra esquina: '))
    yf=int(input('Punto y de contra esquina: '))
    
    if x0 > xf:
        x0,xf = xf,x0
    elif x0 == xf:
        x0, xf= -1
        
    if y0 > yf:
        y0,yf = yf,y0
    elif y0 == yf:
        y0, yf= -1
    
    sub_im= ls[i][x0:xf,y0:yf] ## Windows
    corn0=np.arange(x0,xf+1)
    corn1=np.arange(y0,yf+1)
    sc_img = scale(ls[i]) ## Scaled and casted
    z_arr = np.zeros(ls[i].shape+(3,), sc_img.dtype)
    for t in range(3):
        z_arr[:,:,t]=sc_img  ##Building 3D array
    z_arr[x0,corn1,0],z_arr[xf,corn1,0]=1,1
    z_arr[y0,corn0,0],z_arr[yf,corn0,0]=1,1
    z_arr[x0,corn1,1],z_arr[xf,corn1,1]=0,0
    z_arr[y0,corn0,1],z_arr[yf,corn0,1]=0,0    
    z_arr[x0,corn1,2],z_arr[xf,corn1,2]=0,0
    z_arr[y0,corn0,2],z_arr[yf,corn0,2]=0,0
    axes[i,1]=fig.add_subplot(2,2,2+i*2)

plt.show(block=False)
    
