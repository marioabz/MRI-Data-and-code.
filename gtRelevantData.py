# -*- coding: utf-8 -*-
"""
@author: Mario
"""

import numpy as np
import dicom

class gtRelevantData(object):
    
    def __init__(self, data):
        self.BitsAllocated= data.BitsAllocated
        self.BitsStored= data.BitsStored
        
        try:
            self.StudyComments=data.StuddyComments
        except AttributeError:
            self.StudyComments="No comments"
            
        
data=dicom.read_file('C:/Users/Mario/Desktop/algoritmo/normal 1/IMG-0002-00001.dcm')

patient1= gtRelevantData(data)

