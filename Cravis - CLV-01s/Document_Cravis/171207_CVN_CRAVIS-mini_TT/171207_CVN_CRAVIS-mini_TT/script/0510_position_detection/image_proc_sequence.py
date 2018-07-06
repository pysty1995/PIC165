# -*- coding: utf-8 -*-

"""
module :image_proc_sequence.py
It becomes the image processing sequence module of CRAVIS-mini.
Using image processing function group listed in image_proc_component.py, This file makes an image processing sequence.
When use it in a simple substance; if __name__ = = "__main__": The following sequences are excuted.
"""

__author__ = "cravis-mini"
__version__ = "0.0.0.1"
__date__ = "20161001"

import cv2
import numpy as np
import csv
import math
import time
import sys
import image_proc_component as ipc
import parameter_class

#############
# Function
#############

def func_image_proc_main_sequence(src_img,temp_img,parameter):
    """
    Image processing sequence function
    _@param  src_img.
    _@param  parameter.
    _@return ret. 
    _@return value. 
    _@return output.
    _@return bin_img. 
    """
    
    ret = 0
    output = 0
    value = []
    
    distance_x = 0
    distance_y = 0

    # create gray scale image
    ret,src_gray_img = ipc.func_grayscale(ret,src_img)
    ret,temp_gray_img = ipc.func_grayscale(ret,temp_img)
    
    # execute pattern matching
    ret, match_point = ipc.func_pattern_match(ret,src_gray_img,temp_gray_img)
    print match_point
        
    value.append(match_point[0])
    value.append(match_point[1])
 
    return ret,value,output,src_gray_img

#############
# Main
#############
  
if __name__ == "__main__":
    
    ret = 0
    output = 0
    str_output = "OK"
    parameter_file_name = "parameter.ini"
    
    #  The instance of the parameter file class
    parameter = parameter_class.Parameter()
    # Reading of the parameter file
    ret = parameter.SetParameter(parameter_file_name)
    if ret != 0:
        print "Failure Set Parameter."
        
    # Reading of the image file
    ret,grab_img = ipc.func_imgread(ret,parameter.debug_image_file_name)
    if ret != 0:
        print "Failure Read SRC Image."

    # Reading of the template image file
    ret,temp_img = ipc.func_imgread(ret,parameter.debug_temp_image_file_name)	
    if ret != 0:
        print "Failure Read Template Image."

    # Call the image processing function
    ret,value,output,proc_img = func_image_proc_main_sequence(grab_img,temp_img,parameter)
    
    if ret != 0:
        print "Failure Image Processing."
        output = -1
    
    # Judgement
    if output == 0:
        str_output = "OK"
    
    elif output == 1:
        str_output = "NG"
    
    elif output == -1:
        str_output = "ERR"
    
    # Display image
    cv2.putText(grab_img,"Value:" + str(value),(10,50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
    cv2.rectangle(grab_img,(value[0],value[1]),(value[0] + temp_img.shape[1],value[1] + temp_img.shape[0]),(0,0,255),1)
    cv2.imshow('grab_img',np.array(grab_img,np.uint8))
    cv2.imshow('temp_img',np.array(temp_img,np.uint8))
    
    # Wait a display image
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
