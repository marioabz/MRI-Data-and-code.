# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:50:46 2017

@author: Mario
"""

r=[] #Empty list
a=[] #Empty list

from gtRelevantData import gtRelevantData
from Preprocessing import Preprocessing;
import dicom
from os import listdir
from skimage.morphology import disk
import numpy as np

r=[] #Empty list
img_dimg=[]
img_cleaimg=[]
  
for i in listdir('DCMfiles'):
    for j in listdir('DCMfiles'+'/'+i):
        X=dicom.read_file('DCMfiles'+'/'+i+'/'+j) #Reading DICOM file
        b=gtRelevantData(X) #Instance of gtRelevantData Class
        r.append(b.AcquisitionContrast) #Getting all together in 'r' list
        z=X.pixel_array #z ->X.pixel_array
        a=Preprocessing(z) #Instance of Preprocessing Class
        
        a.add_sp_noise() #Noise
        img_dimg.append(a.psnr(a.img,a.img_over))
        
        a.median_filter(disk(3))
        img_cleaimg.append(a.psnr(a.img,a.img_over))

img_dimg=np.array(img_dimg).reshape((16,2))
img_cleaimg=np.array(img_cleaimg).reshape((16,2))

for x,i in enumerate(r):
    r[x]='T1' in i

e=np.array(r).reshape((16,2))
d=[] #empty list       

for x,[i,j] in enumerate(e):
    if j:
        img_dimg[x,0],img_dimg[x,1]=img_dimg[x,1],img_dimg[x,0]
        img_cleaimg[x,0],img_cleaimg[x,1]=img_cleaimg[x,1],img_cleaimg[x,0]
print('Noise Salt & pepper test')
print('T1       &      T2')

for i in range(16):
    print('paciente & %.3f & %.3f & %.3f & %.3f' % (img_dimg[i,0],img_cleaimg[i,0],
                                         img_dimg[i,1],img_cleaimg[i,1]))
