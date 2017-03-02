__author__ = 'Mario'
import os
import numpy, pylab, pydicom
list=os.listdir()

# filename=os.path.basename(sys.argv[0])    
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
    X.append(pydicom.read_file(inx))

"For displaying all images"
"""for xy in X:
    pylab.imshow(xy.pixel_array, cmap=pylab.cm.gray)
    pylab.show()
    input('Next...')"""
