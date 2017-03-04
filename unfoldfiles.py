__author__ = 'Mario'
import os
import numpy, pylab, dicom

def callImages():

    list=os.listdir()
  
    #list=['4589','.idea','jkj.py', 'ghf.py', '5412'] Testing

    idx=[]
    for x in list:
        hh= list.index(x)

        if x[len(x)-3:len(x)]=='.py' |  x=='.idea':
            idx.append(hh)


    for index in sorted(idx, reverse=True):
        del list[index]

    #Make a big data tuple to handle in one variable all images.
    #Implement for loop for that

    X=[]
    for inx in list:
        X.append(dicom.read_file(inx))
    
    return X

    "For displaying all images"
    """for xy in X:
        pylab.imshow(xy.pixel_array, cmap=pylab.cm.gray)
        pylab.show()
        input('Next...')"""
