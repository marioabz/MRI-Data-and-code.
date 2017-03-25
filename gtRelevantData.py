# -*- coding: utf-8 -*-
"""
@author: Mario
"""

########################################################################
#   Class gtRelevantData: Extract useful data and  perform some useful
#           methods like "get region of interest" from image.
#
#
# This program is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# at your option) any later version.                                   #
#                                                                      #
# This program is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    # 
# along with this program. If not, see <http://www.gnu.org/licenses/>. #
########################################################################


from numpy import zeros
from cv2 import line
from Functions.Scale import scale
from matplotlib.pyplot import hist
from Functions.crop import crop



class gtRelevantData(object):
    
    def __init__(self, data):
        self.Image=                         data.pixel_array
        self.BitsAllocated=                 data.BitsAllocated
        self.BitsStored=                    data.BitsStored
        self.floatImage=                    zeros(data.pixel_array.shape+(3,),float)
        self.floatImage=                    scale(self.Image)
        self.PixelSpacing=                  data.PixelSpacing
        self.PixelArea=                     float(data.PixelSpacing[0])*float(data.PixelSpacing[1])
        self.roi=                           zeros(data.pixel_array.shape+(3,),float)
    
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
            self.PulseSequenceName=         "Not included"
                                                
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
            imgm= line(self.floatImage,point1,point2,color,thickness)
            return imgm
    
    
    def image_hist(self):
        histt,_,_= hist(self.Image.ravel(), bins=200, color='red')
        return hist
    
    def floatImage_hist(self):
        histt,_,_= hist(self.floatImage.ravel(), bins=200, color='red')
        return histt
        
        
    def get_roi(self):
        self.roi= crop(self.Image)
        
        
    def roi_histogram(self):
        histt,_,_= hist(self.roi[:,:,0].ravel(), bins=200,color='red')
        return histt


              
                       