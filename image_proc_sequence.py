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

def func_image_proc_main_sequence(src_img,parameter):
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
    bin_max_val = 255
    serch_area_order = 2
    value = 0
    # 0:OK 1:NG	
    output = 0
    
    # create gray scale image
    ret,roi_img = ipc.func_createRoiimg(ret,src_img,parameter.roi_x,parameter.roi_y,parameter.roi_width,parameter.roi_height)
    
    # create roi image
    ret,gray_img = ipc.func_grayscale(ret,roi_img)

    # create median filter image
    ret,median_img = ipc.func_median_filter(ret,gray_img,parameter.median_kernel_size)
    
    # create binary image
    ret,bin_img = ipc.func_threshold(ret,median_img,parameter.bin_thr,bin_max_val)
        
    # number of white pixels count
    ret,value = ipc.func_countWhitePix(ret,bin_img)
    
    # Judgement
    if value < parameter.area_thr:
        
        # NG
        output = 1
    else:
        # OK
        output = 0
    
    return ret,value,output,bin_img
    
#############
# Main
#############
  
if __name__ == "__main__":
    
    ret = 0
    output = 0
    str_output = "OK"
    parameter_file_name = "parameter.ini"
    
    # The instance of the parameter file class
    parameter = parameter_class.Parameter()
    # Reading of the parameter file
    ret = parameter.SetParameter(parameter_file_name)
    if ret != 0:
        print "Failure Set Parameter."
        
    # Reading of the image file
    ret,grab_img = ipc.func_imgread(ret,parameter.debug_image_file_name)
    if ret != 0:
        print "Failure Read Image."
        
    # Call the image processing function
    ret,value,output,proc_img = func_image_proc_main_sequence(grab_img,parameter)
    
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
    cv2.putText(grab_img,"Output:" + str_output,(10,90),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
    cv2.imshow('grab_img',np.array(grab_img,np.uint8))
    cv2.imshow('proc_img',np.array(proc_img,np.uint8))
    
    # Wait a display image
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()	
