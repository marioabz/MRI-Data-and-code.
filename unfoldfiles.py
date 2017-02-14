__author__ = 'Mario'
import os
import numpy
list=os.listdir()

# filename=os.path.basename(sys.argv[0])    
#list=['4589','.idea','jkj.py', 'ghf.py', '5412'] Testing

idx=[]

for x in list:
    hh= list.index(x)

    if x[len(x)-3:len(x)] == '.py':
        idx.append(hh)

    if x == '.idea':
        idx.append(hh)

for index in sorted(idx, reverse=True):
    del list[index]


#Make a big data tuple to handle in one variable all images.
#Implement for loop for that

data = pydicom.read_file(list[inx])
