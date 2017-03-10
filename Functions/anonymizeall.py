__author__ = 'Mario'

import os, dicom
from dicom.examples.anonymize import anonymize

def anonymize_all(folder):
    
    list= os.listdir(folder) #Folders within gral. folder.
    idx=[] #    Empty list
    anonfolder = folder+'ANMZ'
    os.makedir(anonfolder)
    #To get index of non dicom files
    
    for z in list:  #List of subfolders
        temp_var=folder+'/'+z
        for w in os.listdir(temp_var):
            an_var= temp_var+'/'+w
            data=dicom.read_file(an_var)
            os.remove(an_var)
            data.file_meta.MediaStorageSOPClassUID = '...'
            data.file_meta.MediaStorageSOPInstanceUID = generate_uid()
            data.save_as(an_var)
            
    #Adding necesary tags to properly anonymize all dicom files.
    
    for x in list:
        tempdir=anonfolder+'/'+x+'ANMZ'
        os.makedirs(tempdir)
        tempfold=folder+'/'+x
        for y in os.listdir(tempfold):
            anonymize(tempfold+'/'+y, tempdir+'/'+'anon'+y)
            
    print("All dicom files in this folder have been anonymized")
