# -*- coding: utf-8 -*-
"""
@author: Mario
"""

import numpy as np
import cv2
from Functions.Scale import scale

class gtRelevantData(object):
    
    def __init__(self, data):
        self.Image=                         data.pixel_array
        self.BitsAllocated=                 data.BitsAllocated
        self.BitsStored=                    data.BitsStored
        self.floatImage=                    np.zeros(data.pixel_array.shape+(3,),float)
        self.PixelSpacing=                  data.PixelSpacing
        self.PixelArea=                     float(data.PixelSpacing[0])*float(data.PixelSpacing[1])
        
        try:
            self.PixelPresentation=         data[0x2005,0x140f][0][0x08,0x9205].value
        except KeyError:
            self.PixelPresentation=         'Not included'
         
        try:    
            self.AcquisitionContrast=           data[0x2005,0x140f][0][0x08,0x9209].value
        except KeyError:
            self.AcquisitionContrast=           data.SeriesDescription
                                        
        self.MagneticFieldStrength=         int(data.MagneticFieldStrength)
        
        try:
            self.PulseSequenceName=         data[0x2005,0x140f][0][0x18,0x9005].value
        except KeyError:
            self.PulseSequenceName=         data[0x19,0x109c].value
                                                
        try:                                                
            self.SpectrallySelectedExcitation=  data[0x2005,0x140f][0][0x18,0x9026].value
        except KeyError:
            self.SpectrallySelectedExcitation= 'Not included'     
                                   
        try:
            self.StudyComments=             data.StuddyComments
        except AttributeError:
            self.StudyComments="No comments"
            
            
        def draw_line(self,point1,point2,color,thickness):
            for i in range(3): self.floatImage[:,:,i]= scale(self.Image)
            imgm=cv2.line(self.floatImage,point1,point2,color,thickness)
            return imgm
            
            
            
            
            
            
            
            