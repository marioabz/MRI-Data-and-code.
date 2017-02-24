__author__ = 'Mario'

import numpy as np

def hist(x):

    "Only for 2D datasets"

    x=np.array(x)
    maxx= np.amax(x)
    minx= np.amin(x)

    ls=[]
    for t in range(minx,maxx):
        aux= t == x
        aux.astype(int)
        xsum=np.sum(np.sum(aux))
        ls.append(xsum)

    return ls, minx
