# -*- coding: utf-8 -*-

"""
module :parameter_class.py
It becomes the class with a parameter to set in CRAVIS-mini as a list.
When I want to add a new parameter to CRAVIS-mini, I edit it.
SystemParam　becomes  file pass and various apparatuses parameter.
ImageProcParam becomes the image processing parameter.
"""

__author__ = "cravis-mini"
__version__ = "0.0.0.1"
__date__ = "20161001"

import ConfigParser

class Parameter(object):
    """description of class"""
    # [SystemParam]
    #①add the parameter of the system.
    flag_debug_mode = 0
    flag_save_image = 0
    flag_save_output_data = 0
    flag_disp_image = 0
    light_level = 0
    shutter_speed = 0
    mcp_ether_data_length = 0
    mcp_ether_data_address = 0
    ready_io_no = 0
    ok_io_no = 0
    ng_io_no = 0
    save_image_folder_name = ""
    debug_image_file_name = ""
    debug_temp_image_file_name = ""
    inspect_output_file_name = ""

    # [ImageProcParam]
    #①add the parameter of image processing.
    template_org_point_x = 0
    template_org_point_y = 0
    resolution = 0

    def __init__(self):
        print "Init Parameter"
    
    def SetParameter(self,file_name):
        
        """
        _@param  self       
        _@param  file_name  
        _@return ret       
        """
        
        ret = 0
    
        try:
            inifile = ConfigParser.SafeConfigParser()
            inifile.read(file_name)
            # [SystemParam]
            self.flag_save_image = int(inifile.get("SystemParam","flag_save_image"))
            self.flag_save_output_data = int(inifile.get("SystemParam","flag_save_output_data"))
            self.flag_disp_image = int(inifile.get("SystemParam","flag_disp_image"))
            self.light_level = int(inifile.get("SystemParam","light_level"))
            self.shutter_speed = int(inifile.get("SystemParam","shutter_speed"))
            self.mcp_ether_data_length = int(inifile.get("SystemParam","mcp_ether_data_length"))
            self.mcp_ether_data_address = int(inifile.get("SystemParam","mcp_ether_data_address"))
            self.ready_io_no = int(inifile.get("SystemParam","ready_io_no"))
            self.ok_io_no = int(inifile.get("SystemParam","ok_io_no"))
            self.ng_io_no = int(inifile.get("SystemParam","ng_io_no"))
            self.save_image_folder_name = inifile.get("SystemParam","save_image_folder_name")
            self.debug_image_file_name = inifile.get("SystemParam","debug_image_file_name")
            self.debug_temp_image_file_name = inifile.get("SystemParam","debug_temp_image_file_name")
            self.inspect_output_file_name = inifile.get("SystemParam","inspect_output_file_name")
            
            # [ImageProcParam]
            self.template_org_point_x = int(inifile.get("ImageProcParam","template_org_point_x"))
            self.template_org_point_y = int(inifile.get("ImageProcParam","template_org_point_y"))
            self.resolution = float(inifile.get("ImageProcParam","resolution"))
            
        except:
            ret = -1
            print "Failure Set Parameter."
                
        finally:
            return ret
