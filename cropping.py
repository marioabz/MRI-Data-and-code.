@author: Mario
"""

import numpy as np
import matplotlib.pyplot as plt
import dicom

fig = plt.figure()

data=dicom.read_file('C:/Users/Mario/PycharmProjects/dicomfilesO/1431')       
plt.imshow(data.pixel_array, cmap='gray')

coords=[]

def ifclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print('x = %d, y = %d'%(ix, iy))

    global coords
    coords.append((ix, iy))

    if len(coords) == 2:
        fig.canvas.mpl_disconnect(cid)
    
    return coords


while coords != 2:
    cid= fig.canvas.mpl_connect('button_press_event', ifclick)
    
if coords[0][0] < coords[1][0]:
    x0=coords[0][0], xf=coords[1][0]
elif coords[0][0] > coords[1][0]:
    x0=coords[1][0], xf=coords[0][0]
else:
    x0, xf= -1
    
if coords[0][1] < coords[1][1]:
    y0=coords[0][1], yf=coords[1][1]
elif coords[0][1] > coords[1][1]:
    y0=coords[1][1], yf=coords[0][1]
else:
    y0, yf=-1
