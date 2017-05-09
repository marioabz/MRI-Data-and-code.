# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:12:59 2017

@author: Mario
"""

import numpy as np
from sklearn.cluster import KMeans
from time import time
from Functions.crop import crop
from skimage.morphology import watershed


class Segmentation(object):
    
    def __init__(self,X,clusters=5,max_iter=300,default_centroids=True):
        self.X=                 X
        self.n,self.m=          X.shape
        self.clusters=          clusters
        self.centroids=         np.zeros((self.clusters,3))
        self.max_iter=          max_iter
        self.kmeans=            KMeans(self.clusters, precompute_distances=True)
        self.kmeans_clusters=   np.zeros(self.X.shape,int)
        self.indices=           np.indices((self.n,self.m))
        self.ind_mat=           np.column_stack( (self.indices[0,:,:].reshape(self.n*self.m),
                                                  self.indices[1,:,:].reshape(self.n*self.m),
                                                  self.X.reshape(self.n*self.m)) )
        self.labels=            list(range(self.clusters))
        
        
    def k_means(self):
        start=time()
        self.kmeans_clusters=   self.kmeans.fit(self.ind_mat).labels_.reshape(self.n,self.m)
        end=time()
        print('Elapsed time in seconds: ', end-start)
        return end-start
    
    def quantify_area_mm(self, label, mm):
        qm = np.sum(np.int16(self.image==label))
        return qm*mm
    
    def measure_roi(image,label):
        x=crop(image)
        return np.sum(np.int16(x==label))
        
        
    def biggest_region(self):
        mtx=np.int16(self.X==self.labels[0])
        for i in self.labels[1:]:
            r=np.int16(self.X==i)
            if np.sum(r)>np.sum(mtx): 
                mtx = r
        return i
    
    def def_centroids(self):
        self.centroids=np.column_stack((np.full((self.clusters,3),self.n/2),np.linspace(self.X.min(),self.X.max(),self.clusters)))
    
    
    
    
        
    #def fcm(self):
        
        
        