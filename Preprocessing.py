
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
import numpy as np
from tkinter import Tk
from Functions.sel_range import get_range


class Preprocessing(object):
    
    def __init__(self, x):
        self.s2nR=         0.0
        self.Img =         x
        self.img_stretch=  np.zeros(x.shape, float)


    
    def contrast_stretch(self):
        master= Tk();
        X= get_range(master)
        return exposure.rescale_intensity(self.Img_stretch,in_range=X)
    
    
        
        
        
        
        
        
        
        