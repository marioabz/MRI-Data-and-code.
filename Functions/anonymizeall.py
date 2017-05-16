__author__ = 'Mario'

########################################################################
#   Anonymize function: Function to anonymize dicom files              #
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

import os, dicom
from dicom.examples.anonymize import anonymize
from dicom.UID import generate_uid


def anonymize_all(folder):

    lista= os.listdir(folder) #Folders within gral. folder.
    anonfolder = folder+'anmzd'
    os.mkdir(anonfolder)
        #To get index of non dicom files
        
        #Adding needed tags and hiding institution name.    
    for z in lista:  #List of subfolders
        temp_var=folder+'/'+z
        for w in os.listdir(temp_var):
            an_var= temp_var+'/'+w
            data=dicom.read_file(an_var)
            os.remove(an_var)
            data.file_meta.MediaStorageSOPClassUID = '...'
            data.file_meta.MediaStorageSOPInstanceUID = generate_uid()
            data.InstitutionName='No location'
            data.save_as(an_var)
                    
        #Anonymize files and create NEW folder within the same direction
            
    for x in lista:
        tempdir=anonfolder+'/'+'anonymized-'+x
        os.makedirs(tempdir)
        tempfold=folder+'/'+x
        for y in os.listdir(tempfold):
            anonymize(tempfold+'/'+y, tempdir+'/'+'anon'+y)
                    
    print("All dicom files in this folder have been anonymized")
