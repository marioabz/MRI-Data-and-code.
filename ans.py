# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:31:01 2017

@author: Mario
"""
from gtRelevantData import gtRelevantData
from os import listdir
import numpy as np,dicom

'Expert answers'
ans=['si',      
 'si',
 'p',
 'no',
 'no',
 'no',
 'p',
 'p',
 'p',
 'p',
 'no',
 'no',
 'p',
 'p',
 'p',
 'si',
 'no',
 'p',
 'p',
 'no',
 'no',
 'p',
 'si',
 'no',
 'no',
 'si',
 'si',
 'no',
 'no',
 'p',
 'si',
 'p']
clus=[4, 4, 4, 3, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 4, 4, 4, 3, 3, 4, 4, 4, 4, 4, 4, 3, 3]
print(' & T1 & T2 ')
for i in ans:
    if i=='si':
        ans[ans.index(i)]='\\ding{51}'
    elif i=='no':
        ans[ans.index(i)]='\\ding{55}'
    else:
        ans[ans.index(i)]='--       '
ans=np.array(ans).reshape((16,2))
cont=[]

for i in listdir('DCMfiles'):
    for j in listdir('DCMfiles'+'/'+i):
        cont.append(gtRelevantData(dicom.read_file('DCMfiles'+'/'+i+'/'+j)).AcquisitionContrast)

for x,i in enumerate(cont):
    cont[x]='T1' in i

cont=np.array(cont).reshape((16,2))
clus=np.array(clus).reshape((16,2))

for x,[i,j] in enumerate(cont):
    if j:
        ans[x,0],ans[x,1]=ans[x,1],ans[x,0]


for s in range(16):
    print(s,'&  ', clus[s,0], '&   ', ans[s,0],'&   ',clus[s,0], '&' ,ans[s,1])
    
    
    
        
        
        
    
