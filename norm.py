__author__ = 'Mario'

import sklearn.preprocessing as sklpp
import pylab, os
from hist import hist
from Unfoldfiles import callImages
import numpy
X= callImages(os.listdir())
f=[]
y=[]
for x in X:
  az=np.amax(x)
  ac=np.amin(x)
  f.append(az)
  y.append(ac)

m=numpy.column_stack((numpy.asarray(f),numpy.asarray(y)))
o,p=m.shape

for i in range(len(f)):
  print(m[i,:])
  
  
#for i in X:
  #scaler=sklpp.MinMaxScaler()
  #Xminmax = min_max_scaler.fit_transform(i)

#First it is necesar

#This allows to watch the range of gray intensities to see if normalization could work.
#Pre-processing step

