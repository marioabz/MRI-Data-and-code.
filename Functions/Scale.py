# -*- coding: utf-8 -*-
"""
@author: Mario
"""
########################################################################
#   Scale function: Casting an array image to float without changing   # 
#                the limits
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

import numpy as np

def scale(X):
    
    A=  np.array(X)
    mx= np.amax(X)
    mn= np.amin(X)
    A=  (X-mn)/(mx-mn)
    
    return np.float32(A)
