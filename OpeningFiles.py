#Python 3.4.3
#Dicom package https://github.com/darcymason/pydicom
#Open DICOM file basics.


import pydicom
import numpy #To handle the array of bytes that contains the image.


lst=pydicom.read_file("6293")
