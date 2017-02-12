#Python 3.4.3
#Dicom package https://github.com/darcymason/pydicom
#Open DICOM file basics.

import pydicom
import matplotlib
matplotlib.use('TkAgg') #For windows use: TkAgg
import pylab

lst=pydicom.read_file("6293")

#To know the image dimensions
print('Dimensions of image are: %s' %(lst.pixel_array.shape,))

#Displaying pixel array is an image
pylab.imshow(lst.pixel_array, cmap=pylab.cm.gray)
pylab.show()

#Image "Test1.png" is the result of this test.
