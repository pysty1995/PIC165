# -*- coding: utf-8 -*- 
"""
module :main_sequence.py
It becomes the main sequence module of CRAVIS-mini.
Using cmlib function group, This file control each apparatus.
The main image processing calls func_image_proc_main_sequence function of image_proc_sequence.py.
"""
__author__ = "cravis-mini"
__version__ = "0.0.0.1"
__date__ = "20161001"

import cv2
import numpy as np
import csv
import math
import time
from datetime import datetime
import sys
import logging
import image_proc_sequence as ips
import image_proc_component as ipc
import parameter_class
import cmlib

#############
# Function
#############

def func_error_action(func_name,error_code,error_logger):
    """
    Error processing function
    @param  func_name       
    @param  error_code      
    @param  error_logger    
    """
    if error_code <= 100000:
        #shift to alert processing
        func_alert_action(func_name,error_code,error_logger)

        return

    else:
        #Create error documentation
        msg = func_name + " is Error." + " ErrorCode : " + str(error_code)
        error_logger.error(msg)
        #IO apparatus is clear
        ret = cmlib.OutClear()

        print "Please restart  CravisMini."

        exit()

def func_alert_action(func_name,error_code,error_logger):
    """
    Alert processing function
    @param  func_name
    @param  error_code
    @param  error_logger
    """
    #Create alert documentation
    msg = func_name + " is ALERT." + " ALERTCode : " + str(error_code)
    error_logger.error(msg)
    
    return

def func_save_image(src_img,save_file_name):
    """
    Save Image function
    @param  src_img             
    @param  save_file_name      
    """
    try:
        cv2.imwrite(save_file_name, np.array(src_img,np.uint8))
    except:
        print "Failure InspectSave Image."
    finally:
        return

def func_create_error_logger(error_log_file_name):
    """
    Error log generation function
    @param  error_log_file_name
    @return error_logger
    """
    #Instance making of the error log variable
    error_logger = logging.getLogger("error_logger")
    error_logger.setLevel(logging.DEBUG)

    #Format preparations for log description
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(formatter)
    
    #Registration of the handler
    error_logger.addHandler(sh)
    
    #Registration of the error log file
    err_fh = logging.FileHandler(filename= error_log_file_name)
    err_fh.setLevel(logging.DEBUG)
    err_fh.setFormatter(formatter)

    error_logger.addHandler(err_fh)

    return error_logger
    
def func_create_inspect_output_logger(inspect_output_file_name):
    """
    Result log generation function
    @param  output_file_name        
    @return insp_output_logger      
    """
    #Instance making of the result log variable
    insp_output_logger = logging.getLogger("insp_output_logger")
    insp_output_logger.setLevel(logging.DEBUG)
    
    #Format preparations for log description
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(formatter)
    
    #Registration of the handler
    insp_output_logger.addHandler(sh)
    
    #Registration of the test result log file
    io_fh = logging.FileHandler(filename= inspect_output_file_name)
    io_fh.setLevel(logging.DEBUG)
    io_fh.setFormatter(formatter)

    insp_output_logger.addHandler(io_fh)

    return insp_output_logger

#############
# Main
#############
if __name__ == "__main__":
    ret = 0
    inspect_no = 0
    inspect_time = ""
    output = 0
    str_output = "OK"
    parameter_file_name = "/home/pi/CravisMini/python_proc/parameter.ini"
    error_log_file_name = "error_log.txt"

    #Setting of the error logger
    error_logger = func_create_error_logger(error_log_file_name)

    #Reading of the parameter file
    parameter = parameter_class.Parameter()

    ret = parameter.SetParameter(parameter_file_name)
    if ret != 0:
        func_error_action("parameter.SetParameter",ret,error_logger)
        
    #Setting of the result logger
    insp_output_logger = func_create_inspect_output_logger(parameter.inspect_output_file_name)

    #Initialization of various apparatuses
    ret = cmlib.Init()
    if ret != 0:
        func_error_action("cmlib.Init",ret,error_logger)

    #Light control of the illumination
    ret = cmlib.LightPwm(parameter.light_level)
    if ret != 0:
        func_error_action("cmlib.LightPwm",ret,error_logger)

    #Setting of the shutter speed
    ret = cmlib.ShutterSpeedSet(parameter.shutter_speed)
    if ret != 0:
        func_error_action("cmlib.ShutterSpeedSet",ret,error_logger)

    #The input and output of the IO apparatus is clear
    ret = cmlib.OutClear()
    if ret != 0:
        func_error_action("cmlib.OutClear",ret,error_logger)

    # Reading of the template image file
    ret,temp_img = ipc.func_imgread(ret,parameter.debug_temp_image_file_name)	
    if ret != 0:
        print "Failure Read Template Image."
        
    while 1:
        #Setup of the Ready signal
        ret = cmlib.SetIO(parameter.ready_io_no,1)
        if ret != 0:
                func_error_action("cmlib.SetIO(parameter.ready_io_no,1)",ret,error_logger)

        #Inspection start trigger wait
        print "Wait Tirgger"
        #ret = cmlib.WaitTrigger()
        raw_input(">>>")
        if ret != 0:
            func_error_action("cmlib.WaitTrigger",ret,error_logger)

        #Of the Ready signal stand, and lower it
        ret = cmlib.SetIO(parameter.ready_io_no,0)
        if ret != 0:
            func_error_action("cmlib.SetIO(parameter.ready_io_no,0)",ret,error_logger)

        #The acquisition of the inspection start time
        inspect_time = datetime.today()

        #Illumination lighting
        ret = cmlib.LightOn()
        if ret != 0:
            func_error_action("cmlib.LightOn",ret,error_logger)

        #Grab image
        ret,grab_img = cmlib.GrabFrameEx()
        if ret != 0:
            func_error_action("cmlib.GrabFrameEx()",ret,error_logger)

        #Save Image
        if parameter.flag_save_image == 1:
            func_save_image(grab_img,parameter.save_image_folder_name + "\\" + str(inspect_time.year) + "_" + str(inspect_time.month) + "_" + str(inspect_time.day) + "_" + str(inspect_time.hour) + str(inspect_time.minute) + str(inspect_time.second) + "_GrabImg.png")

        #Illumination lights out
        ret = cmlib.LightOff()
        if ret != 0:
            func_error_action("cmlib.LightOff()",ret,error_logger)

        #Image processing execute
        ret,value,output,proc_img = ips.func_image_proc_main_sequence(grab_img,temp_img,parameter)

        if ret != 0:
            func_error_action("ips.func_image_proc_main_sequenc",ret,error_logger)
            output = -1
        
        #judgement
        if output == 0:
            #The ON output of the parameter.ok_io_no port
            ret = cmlib.SetIO(parameter.ok_io_no,1)
            if ret != 0:
                    func_error_action("cmlib.SetIO(parameter.ok_io_no,1)",ret,error_logger)
            #Waiting for output 0.1[sec]
            time.sleep(0.1)
            #The OFF output of the parameter.ok_io_no port
            ret = cmlib.SetIO(parameter.ok_io_no,0)
            if ret != 0:
                    func_error_action("cmlib.SetIO(parameter.ok_io_no,0)",ret,error_logger)
        
            str_output = "OK"

        elif output == 1:
            #The ON output of the parameter.ng_io_no port
            ret = cmlib.SetIO(parameter.ng_io_no,1)
            if ret != 0:
                    func_error_action("cmlib.SetIO(parameter.ng_io_no,1)",ret,error_logger)
            #Wait Time 0.1[sec]
            time.sleep(0.1)
            #The OFF output of the parameter.ng_io_no port
            ret = cmlib.SetIO(parameter.ng_io_no,0)
            if ret != 0:
                func_error_action("cmlib.SetIO(parameter.ng_io_no,0)",ret,error_logger)

            str_output = "NG"

        elif output == -1:
            #The ON output of the parameter.ng_io_no port
            ret = cmlib.SetIO(parameter.ng_io_no,1)
            if ret != 0:
                    func_error_action("cmlib.SetIO(parameter.ng_io_no,1)",ret,error_logger)
            #Wait Time 0.1[sec]
            time.sleep(0.1)
            #The OFF output of the parameter.ng_io_no port
            ret = cmlib.SetIO(parameter.ng_io_no,0)
            if ret != 0:
                func_error_action("cmlib.SetIO(parameter.ng_io_no,0)",ret,error_logger)

            str_output = "ERR"

        #Save result log
        if parameter.flag_save_output_data == 1:
            insp_output_logger.info(str_output)

        #Display image
        if parameter.flag_disp_image == 1:
            cv2.putText(grab_img,"Value:" + str(value),(10,50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
            cv2.rectangle(grab_img,(value[0],value[1]),(value[0] + temp_img.shape[1],value[1] + temp_img.shape[0]),(0,0,255),1)
            cv2.imshow('grab_img',np.array(grab_img,np.uint8))
            ##DispWait[msec]
            cv2.waitKey(1000)

    cv2.destroyAllWindows()
