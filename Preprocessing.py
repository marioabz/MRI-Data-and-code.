
"""
@author: Mario
"""
########################################################################
#   Class Preprocessing: Performs enhancement techniques to increase   #
#   image quality.                                                     #
#                                                                      #
#                                                                      #
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

import numpy as np
from scipy.stats import signaltonoise as s2nR
from skimage import exposure
from numpy import zeros, mean
from tkinter import Tk
from Functions.sel_range import get_range
from Functions.mask import select_threshold_mask
from skfuzzy import defocus_local_means
from skfuzzy.image import nmse
from skimage.filters import sobel,median
from skimage.filters.rank import enhance_contrast
from skimage.morphology import disk,square,erosion,dilation,opening
from skimage.util import random_noise
from Functions.Scale import scale
from numpy import uint16
from scipy import ndimage as ndi
from Functions.crop import crop


class Preprocessing(object):
    
    def __init__(self, x):
        self.s2nR=         0.0
        self.img =         x
        self.img_over=     x
        self.img_reset=    x
        self.type=         x.dtype
    
    def contrast_stretch(self):
        master= Tk();
        X= get_range(master);
        self.img_stretch= exposure.rescale_intensity(self.Img,in_range=X)
    
    def s2nR(self):
        self.s2nR=s2nR(self.Img, axis=None) 
        
    def histogram_eq(self, _mask_sltr=True):
        if _mask_sltr == True:
            thrld= select_threshold_mask(self.img)
        else:
            thrld= mean(self.img)
        self.img_over= exposure.equalize_hist(self.img ,mask=self.img>thrld)
    
    def adaptive_hist(self,kernel=15):
        self.img_over= np.int16(exposure.equalize_adapthist(np.uint16(self.img),kernel_size=kernel)*self.img.max())
    
    def nmse(self,x,y):
        return nmse(x,y)
    
    def dlm(self):
        self.img_over= defocus_local_means(self.img)
    
    def contrast_enhancement(self, local_mtx=disk(5)):
        self.img_over= enhance_contrast(uint16(self.img), local_mtx,mask=self.img>self.img.mean())
    
    def detect_borders(self):
        return sobel(self.img)
    
    def add_sp_noise(self,percentage=0.5):
        self.img_over= uint16(random_noise(scale(self.img), mode='s&p', salt_vs_pepper=percentage)*self.img.max())
    
    def median_filter(self,struct=disk(5)):
        self.img_over= median(uint16(self.img), selem=struct)
        
    def erosion(self, struct= disk(5)):
        self.img_over=erosion(self.img, selem=struct)
        
    def reset_img(self):
        self.img, self.img_over= self.img_reset, self.img_reset
        
    def apply_same_img(self):
        self.img=self.img_over
    
    def psnr(self,img, p_img):
        emc=1/(img.shape[0]*img.shape[1])*np.sum((scale(img)-scale(p_img))**2)
        psnr=10*np.log10(1/emc)
        return psnr
    
    def contrast_measure(self):
        a=1/(self.img.shape[0]*self.img.shape[1]-1)
        return np.sqrt(a*np.sum( (self.img_over-self.img_over.mean())**2) )
    
    def b2odt(self):
        self.img_over=np.int16(self.img_over*self.img.max())
        
    def remove_skull(self, b_img, struct=disk(3)):
        a=[]
        F=erosion(b_img, selem=struct)
        lbl=ndi.label(F)[0]
        for i in range(lbl.max()-1):
            a.append(np.sum(lbl==(i+1)))
        c=a
        a=np.array(a)
        clas=c.index(a.max())+1
        E= ndi.binary_fill_holes(lbl==clas)
        E=dilation(E,selem=struct)
        
        return self.img * E
    
    def get_roi(self): #Cropping region of interest out of the image.
        roi= crop(self.img)
        self.img_over= self.img[roi[0][1]:roi[1][1],roi[0][0]:roi[1][0]]
