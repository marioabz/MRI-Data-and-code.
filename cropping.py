# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:06:07 2017
@author: Mario
"""

import cv2, dicom
import numpy as np

from tkinter import filedialog
import matplotlib.pyplot as plt

def scale(X):
    A=np.array(X)
    mx=np.amax(X)
    mn=np.amin(X)
    A=(X-mn)/(mx-mn)
    return np.float32(A)

coords = []
cropping = False
folder= filedialog.askopenfilename()
    
def ccrop(event, x, y, flags, param):
	global coords, cropping   
	if event == cv2.EVENT_LBUTTONDOWN:
		coords = [(x, y)]
		cropping = True
	elif event == cv2.EVENT_LBUTTONUP:
		coords.append((x, y))
		cropping = False 
		cv2.rectangle(image, coords[0], coords[1], (0, 0, 255), 2)
		cv2.imshow("Patient", image)
        
image3 = scale(dicom.read_file(folder).pixel_array)
image=np.zeros(image3.shape+(3,),image3.dtype)

for z in range(3):
    image[:,:,z]=image3
    
clone = image.copy()
cv2.namedWindow("Patient")
cv2.setMouseCallback("Patient", ccrop)

while True:
	cv2.imshow("Patient", image)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("r"):
		image = clone.copy()
	elif key == ord("c"):
		break
    
[x0,y0]=coords[0]
[xf,yf]=coords[1]

if x0 > xf:
    x0,xf = xf,x0
elif x0 == xf:
    x0, xf= -1
if y0 > yf:
    y0,yf = yf,y0
elif y0 == yf:
    y0, yf= -1
 
if len(coords) == 2:
    	roi = clone[y0:yf,x0:xf]
    	cv2.imshow("Region of Interest", roi)
    	cv2.waitKey(0)
    

cv2.destroyAllWindows()
axes = np.zeros((1, 3), dtype=np.object)

d=np.where(image[:,:,2] == 255)
image[d[0],d[1],2]=1

fig=plt.figure(figsize=(12,6))
im=axes[0,0]=fig.add_subplot(1,3,1)
roiim=axes[0,1]=fig.add_subplot(1,3,2)
im.set_axis_off()
im.set_title('Imagen original',fontsize=10)
roiim.set_title('Regíon de interés',fontsize=10)
roiim.set_axis_off()
axes[0,0].imshow(image)
axes[0,1].imshow(roi,cmap='gray')
f=axes[0,2]=fig.add_subplot(1,3,3)
axes[0,2].hist(roi.ravel(),bins=150,color='blue')
f.set_title('Histograma de región de interés',fontsize=10)


