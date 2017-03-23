# -*- coding: utf-8 -*-
"""
@author: Mario
"""

import numpy as np
import cv2
from Functions.Scale import scale
import matplotlib.pyplot as plt


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
    
    
    def image_histogram(self):
        plt.hist(self.Image.ravel(), bins=100, color='red')
        
        
    def get_roi(self):
        
        image=self.floatImage
        
        def ccrop(event, x, y, flags, param):
            global coords, cropping   
            if event == cv2.EVENT_LBUTTONDOWN:
                coords = [(x, y)]
                cropping = True
            elif event == cv2.EVENT_LBUTTONUP:
                coords.append((x, y))
                cropping = False 
                cv2.rectangle(self.floatImage, coords[0], coords[1], (0, 0, 255), 2)
                cv2.imshow("Patient", image)
        clone = self.floatImage.copy()
        cv2.namedWindow("Patient")
        cv2.setMouseCallback("Patient", ccrop)
        
        while True:
        	cv2.imshow("Patient", image)
        	key = cv2.waitKey(1) & 0xFF
        	if key == ord("r"):
        		image = clone.copy()
        	elif key == ord("c"):
        		break
    
        [x0,y0]=coords[0]
        [xf,yf]=coords[1]

        if x0 > xf:
            x0,xf = xf,x0
        elif x0 == xf:
            x0, xf= -1
        if y0 > yf:
            y0,yf = yf,y0
        elif y0 == yf:
            y0, yf= -1
        
        if len(coords) == 2:
        	roi = clone[y0:yf,x0:xf]
        	cv2.imshow("Region of Interest", roi)
        	cv2.waitKey(0)
            
        

                
    
    
            
            
            
            
            
            
            
            