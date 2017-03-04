__author__ = 'Mario'

from hist import hist
import dicom
import pylab

im=dicom.read_file('6924')
im=im.pixel_array

h, minx =hist(im)

hx=list(range(1,len(h)))

pylab.plot(h)
pylab.show()


