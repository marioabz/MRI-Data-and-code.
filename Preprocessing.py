
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
from skimage import exposure, rank
from numpy import zeros, mean
from tkinter import Tk
from Functions.sel_range import get_range
from Functions.mask import select_threshold_mask
from skfuzzy import defocus_local_means
from skfuzzy.image import nmse
from skimage.filters import sobel



class Preprocessing(object):
    
    def __init__(self, x):
        self.s2nR=         0.0
        self.Img =         x
        self.img_stretch=  zeros(x.shape, float)
        self.defocus_img=  zeros(x.shape, float)
    
    def contrast_stretch(self):
        master= Tk();
        X= get_range(master);
        self.img_stretch= exposure.rescale_intensity(self.Img,in_range=X)
    
    def s2nR(self):
        self.s2nR=s2nR(self.Img, axis=None) 
        
    def histogram_eq(self, S, _mask_sltr=True):
        if _mask_sltr == True:
            thrld= select_threshold_mask(S)
        else:
            thrld= mean(S)
        return exposure.equalize_hist(S,mask=S>thrld)
    
    def adaptive_hist(self,img):
        return exposure.equalize_adapthist(img)
    
    def nmse(self,x,y):
        return nmse(x,y)
    
    def dlm(self):
        return defocus_local_means(self.Img)
    
    def contrast_enhancement(self):
        return 
    
    def detect_borders(self):
        
    
    
        



        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        