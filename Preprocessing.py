
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
from skimage.morphology import disk,square
from skimage.util import random_noise

class Preprocessing(object):
    
    def __init__(self, x):
        self.s2nR=         0.0
        self.img =         x
        self.img_over=     x
    
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
    
    def adaptive_hist(self,kernel=3):
        self.img_over= exposure.equalize_adapthist(self.img,kernel_size=kernel)
    
    def nmse(self,x,y):
        return nmse(x,y)
    
    def dlm(self):
        self.img_over= defocus_local_means(self.Img)
    
    def contrast_enhancement(self, local_mtx=disk(5)):
        self.img_over= enhance_contrast(self.Img, local_mtx)
    
    def detect_borders(self):
        return sobel(self.Img)
    
    def add_sp_noise(self,percentage=0.5):
        self.img_over= random_noise(self.Img, mode='s&p', salt_vs_pepper=percentage)
    
    def median_filter(self,struct=disk(5)):
        self.img_over= median(self.Img, selem=struct)
    
    
    
    
        



        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        