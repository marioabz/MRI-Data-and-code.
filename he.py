# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:23:41 2017

@author: Mario
"""

from gtRelevantData import gtRelevantData
from Preprocessing import Preprocessing;
import dicom
from os import listdir
import numpy as np

t,y,h=[],[],[]

for i in listdir('DCMfiles'):
    for j in listdir('DCMfiles'+'/'+i):
        X=dicom.read_file('DCMfiles'+'/'+i+'/'+j)
        z=X.pixel_array
        a=Preprocessing(z)
        y.append(a.contrast_measure())
        a.histogram_eq(False)
        a.b2odt()
        t.append(a.contrast_measure())
        f=gtRelevantData(X)
        h.append(f.AcquisitionContrast)
        
t=np.array(t).reshape((16,2))
y=np.array(y).reshape((16,2))

for x,i in enumerate(h):
    h[x]='T1' in i
     
e=np.array(h).reshape((16,2))

print('Normal image Vs. HE Image')
print('T1       &      T2')

for i in range(16):
    print('paciente%i & %.3f & %.3f & %.3f & %.3f' % (i,y[i,0],t[i,0], y[i,1],t[i,1]))
    
    
