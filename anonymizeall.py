__author__ = 'Mario'

import os
from dicom.examples.anonymize import anonymize

list= os.listdir()

idx=[] #    Empty list

#To get index of non dicom files
for x in list:
    hh= list.index(x)
    if x[len(x)-3:len(x)] == '.py':
        idx.append(hh)
    if x == '.idea':
        idx.append(hh)

#Erase non-dicom files
for index in sorted(idx, reverse= True):
    del list[index]

for x in list:
    anonymize(x, 'anon'+x)

print("All dicom files in this folder have been anonymized")
