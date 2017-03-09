__author__ = 'Mario'

import os
from dicom.examples.anonymize import anonymize

def anonymize_all(folder):
    
    list= os.listdir(folder)
    idx=[] #    Empty list
    anonfolder = folder+'ANMZ'
    os.makedir(anonfolder)
    #To get index of non dicom files
    
    for x in list:
        tempdir=anonfolder+'/'+x+'ANMZ'
        os.makedirs(tempdir)
        tempfold=folder+'/'+x
        for y in os.listdir(tempfold):
            anonymize(tempfold+'/'+y, tempdir+'/'+'anon'+y)
            
    print("All dicom files in this folder have been anonymized")
