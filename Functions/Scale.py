# -*- coding: utf-8 -*-
"""
@author: Mario
"""
import numpy as np

def scale(X):
    
    A=  np.array(X)
    mx= np.amax(X)
    mn= np.amin(X)
    A=  (X-mn)/(mx-mn)
    
    return np.float32(A)
