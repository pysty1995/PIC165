# -*- coding: utf-8 -*-
"""
module :image_proc_component.py
It becomes the image processing component module of CRAVIS-mini.
This function is called in image_proc_sequence.py.
In this function group, a function of OpenCV is wrapped by an exception handling.
"""
__author__ = "cravis-mini"
__version__ = "0.0.0.1"
__date__ = "20161001"

import cv2
import numpy as np
import math
from scipy import ndimage
from scipy import optimize
import scipy
import warnings

#############
# Function
#############
def func_imgread(ret,file_name):
    """
    Image reading function
    @param  ret　　　　　　　　　　　　　　　　
    @param  file_name　　　　　　　　　　  
    @return ret  　　　　　　　　　　      
    @return src_img  　　　　　　　　　　  
    """
    if ret != 0:
        return ret,0

    try:
        src_img = cv2.imread(file_name)

    except:
        ret = 10101
        return ret,0

    return ret,src_img


def func_createRoiimg(ret,src_img,roi_x,roi_y,roi_width,roi_height):
    """
    create roi image function
    @param  ret　　　　　　　　　　　　　　　　
    @param  src_img 　　　　　　　　　　   
    @param  roi_x 　　　　　　　　　　     
    @param  roi_y 　　　　　　　　　　     
    @param  roi_width　　　　　　　　　　  
    @param  roi_height　　　　　　　　　　 
    @return ret  　　　　　　　　　　      
    @return roi_img   　　　　　　　　　　 
    """
    if ret != 0:
        return ret,0

    try:
        roi_img = src_img[roi_y : roi_y + roi_height , roi_x : roi_x + roi_width]

    except:
        ret = 10102
        return ret,0

    return ret,roi_img


def func_grayscale(ret,src_img):
    """
    create gray scale image function
    @param  ret                  
    @param  src_img              
    @return ret                  
    @return gray_img             
    """
    if ret != 0:
        return ret,0

    try:
        gray_img = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

    except:
        ret = 10201
        return ret,0

    return ret,gray_img


def func_threshold(ret,src_img,threshold,maxval):
    """
    create binary image function
    @param  ret
    @param  src_img               
    @param  threshold             
    @param  maxval                
    @return ret                   
    @return roi_img               
    """
    if ret != 0:
        return ret,0

    try:
        threshold_img = cv2.threshold(src_img,threshold,maxval,cv2.THRESH_BINARY)[1]

    except:
        ret = 10202
        return ret,0

    return ret,threshold_img


def func_blur_filter(ret,src_img,blur_kernel_size):
    """
    create blur filter image function
    @param  ret                   
    @param  src_img               
    @param  blur_kernel_size      
    @return ret                   
    @return blur_img              
    """
    if ret != 0:
        return ret,0

    try:
        blur_img = cv2.blur(src_img,blur_kernel_size)

    except:
        ret = 10203
        return ret,0

    return ret,blur_img


def func_gaussian_blur_filter(ret,src_img,gaussian_kernel_size,sigmaX):
    """
    create Gaussian blur filter image function
    @param  ret                   
    @param  src_img               
    @param  gaussian_kernel_size  
    @param  sigmaX                
    @return ret                   
    @return gaussianblur_img      
    """ 
    if ret != 0:
        return ret,0

    try:
        gaussianblur_img = cv2.GaussianBlur(src_img,gaussian_kernel_size,sigmaX)

    except:
        ret = 10204
        return ret,0

    return ret,gaussianblur_img
 
   
def func_bilateral_filter(ret,src_img,bilateral_d,bilateral_sigmaColor,bilateral_sigmaSpace):
    """
    create bilateral blur filter image function
    @param  ret                   
    @param  src_img               
    @param  bilateral_d           
    @param  bilateral_sigmaColor  
    @param  bilateral_sigmaSpace  
    @return ret                   
    @return gaussianblur_img      
    """
    if ret != 0:
        return ret,0

    try:
        bilateral_img = cv2.bilateralFilter(src_img,bilateral_d,bilateral_sigmaColor,bilateral_sigmaSpace)

    except:
        ret = 10205
        return ret,0

    return ret,bilateral_img

    
def func_median_filter(ret,src_img,median_kernel_size):
    """
    create median blur filter image function
    @param  ret                   
    @param  src_img               
    @param  median_kernel_size    
    @return ret                   
    @return median_img            
    """
    if ret != 0:
        return ret,0

    try:
        median_img = cv2.medianBlur(src_img,median_kernel_size)

    except:
        ret = 10206
        return ret,0

    return ret,median_img


def func_sobel_filter(ret,src_img,sobel_ddepth,sobel_dx,sobel_dy):
    """
    create sobel filter image function
    @param  ret                   
    @param  src_img               
    @param  sobel_ddepth          
    @param  sobel_dx              
    @param  sobel_dy              
    @return ret                   
    @return sobel_img            　
    """
    if ret != 0:
        return ret,0

    try:
        sobel_img = cv2.Sobel(src_img,sobel_ddepth,sobel_dx,sobel_dy)

    except:
        ret = 10207
        return ret,0

    return ret,sobel_img


def func_laplacian_filter(ret,src_img,laplacian_ddepth):
    """
    create sobel filter image function
    @param  ret                   
    @param  src_img               
    @param  laplacian_ddepth      
    @return ret                   
    @return lap_img               
    *このフィルタは４近傍で計算されます
    """
    if ret != 0:
        return ret,0

    try:
        lap_img = cv2.Laplacian(src_img,laplacian_ddepth)

    except:
        ret = 10208
        return ret,0

    return ret,lap_img


def func_dilate_filter(ret,src_img,dilate_kernel):
    """
    create dilate filter image function
    @param  ret                   
    @param  src_img               
    @param  dilate_kernel         
    @return ret                   
    @return dilate_img            
    """
    if ret != 0:
        return ret,0

    try:
        kernel = np.ones((dilate_kernel, dilate_kernel))
        dilate_img = cv2.dilate(src_img,kernel)

    except:
        ret = 10209
        return ret,0

    return ret,dilate_img


def func_erode_filter(ret,src_img,erode_kernel):
    """
    create erode filter image function
    @param  ret                   
    @param  src_img               
    @param  erode_kernel          
    @return ret                   
    @return erode_img             
    """
    if ret != 0:
        return ret,0

    try:
        kernel = np.ones((erode_kernel, erode_kernel))
        erode_img = cv2.erode(src_img,kernel)

    except:
        ret = 10210
        return ret,0

    return ret,erode_img


def func_filter_2d_img(ret,src_img,kernel):
    """
    create filter_2d image function
    @param  ret                   
    @param  src_img               
    @param  kernel                
    @return filter_2d_img         
    """
    if ret != 0:
        return ret,0

    try:
        filter_2d_img = cv2.filter2D(src_img,-1,kernel)

    except:
        ret = 10211
        return ret,0

    return ret,filter_2d_img


def func_RedColor_img(ret,src_img):
    """
    create red extraction image image function
    @param  ret                   
    @param  src_img               
    @return ret                   
    @return red_img               
    """
    if ret != 0:
        return ret,0

    try:
        red_img = src_img[:,:,2]

    except:
        ret = 10212
        return ret,0

    return ret,red_img


def func_GreenColor_img(ret,src_img):
    """
    create green extraction image image function
    @param  ret                   
    @param  src_img               
    @return ret                   
    @return green_img             
    """
    if ret != 0:
        return ret,0

    try:
        green_img = src_img[:,:,0]

    except:
        ret = 10213
        return ret,0

    return ret,green_img


def func_BlueColor_img(ret,src_img):
    """
    create blue extraction image image function
    @param  ret                   
    @param  src_img               
    @return ret                   
    @return blue_img              
    """
    if ret != 0:
        return ret,0

    try:
        blue_img = src_img[:,:,1]

    except:
        ret = 10214
        return ret,0

    return ret,blue_img


def func_rgb_to_lab(ret,src_img):
    """
    RGB → L*a*b* color space conversion function
    @param  ret                   
    @param  src_img               
    @return ret                   
    @return lab_img               
    """
    if ret != 0:
        return ret,0

    try:
        lab_img = cv2.cvtColor(src_img,cv2.COLOR_RGB2LAB)

    except:
        ret = 10215
        return ret,0

    return ret,lab_img


def func_labels(ret,src_img):
    """
    labeling function
    @param  ret                   
    @param  src_img               
    @return ret                   
    @return labels                
    @return nb                    
    """
    if ret != 0:
        return ret,0,0

    try:
        labels , nb = ndimage.label(src_img)

    except:
        ret = 10216
        return ret,0,0

    return ret,labels,nb


def func_calc_feature(ret,bin_img,labels):
    """
    Blob analysis function
    @param  ret                   
    @param  bin_img               
    @param  labels                
    @return ret                   
    @return areas                 
    @return centoroid
    """
    if ret != 0:
        return ret,0,0

    try:
        #area
        areas = np.array(ndimage.sum(bin_img / bin_img.max(),labels,xrange(1,labels.max() + 1)))
        #centroid
        centroid = np.array(ndimage.center_of_mass(bin_img / bin_img.max(),labels,xrange(1,labels.max() + 1)))

    except:
        ret = 10217
        return ret,0,0

    return ret,areas,centroid


def func_blob_select(ret,areas,serch_area_order,bin_maxval,labels):
    """
    Making of the image which only the blob of any label number that I set left function
    @param  ret                   
    @param  areas                 
    @param  serch_area_order      
    @param  bin_maxval            
    @param  labels                
    @return ret                   
    @remove_img                   
    """
    if ret != 0:
        return ret,0

    try:
        # CreateLabelIndexList
        label_index_list = [x for x in range(1,areas.size + 1)]
        # Marge LabelIndex And AreasList
        list = [[label_index_list[i],areas[i]] for i in range(0,areas.size)]
        # Sort
        sort_list = sorted(list,key=lambda i: i[1])
        # SerchSelectIndex
        serch_index = sort_list[areas.size - serch_area_order][0]
        # CreateRemobeImg
        remove_img = labels == serch_index
        remove_img = bin_maxval * remove_img
        remove_img = np.array(remove_img,np.uint8)

    except:
        ret = 10218
        return ret,0

    return ret,remove_img


def func_match_shapes(ret,ob1,ob2,method=1):
    """
    Shape matching processing function
    @param  ret                   
    @param  ob1                  
    @param  ob2                   
    @param  method               
    @return ret                  
    @return sum(s)                
    """
    if ret != 0:
        return ret,0

    try:
        ma = cv2.moments(ob1)
        hua = cv2.HuMoments(ma)

        mb = cv2.moments(ob2)
        hub = cv2.HuMoments(mb)

        s = []

        if method == 1:
            for i in range(0,7):
                s.append(abs(1/math.copysign(math.log(abs(hua[i])),hua[i])-1/math.copysign(math.log(abs(hub[i])),hub[i])))
            return ret,sum(s)

        if method == 2:
            for i in range(0,7):
                s.append(abs(math.copysign(math.log(abs(hua[i])),hua[i])-math.copysign(math.log(abs(hub[i])),hub[i])))
            return ret,sum(s)

        if method == 3:
            for i in range(0,7):
                s.append(abs((math.copysign(math.log(abs(hua[i])),hua[i])-math.copysign(math.log(abs(hub[i])),hub[i]))/math.copysign(math.log(abs(hua[i])),hua[i])))
            return ret,sum(s)

    except:
        ret = 10219
        return ret,0


def func_pattern_match(ret,src_img,template_img):
    """
    Pattern matching processing function
    @param  ret                   
    @param  src_img               
    @param  template_img          
    @return ret                   
    @return match_point           
    """
    if ret != 0:
        return ret,0

    try:
        score = cv2.matchTemplate(src_img,template_img,cv2.TM_SQDIFF)  #OpenCV2.4 method = cv2.cv.CV_TM_SQDIFF
        macth_score_info = cv2.minMaxLoc(score)
        match_point = macth_score_info[2]

    except:
        ret = 10220
        return ret,0

    return ret,match_point


def func_rotate_img(ret,src_img,src_w,src_h,angle):
    """
    Rotary conversion of the image function
    @param  ret                   
    @param  src_img               
    @param  src_w                 
    @param  src_h                 
    @param  angle                 
    @return ret                   
    @return rotate_img            
    """
    if ret != 0:
        return ret,0

    try:
        M = cv2.getRotationMatrix2D((src_w/2,src_h/2),angle,1)
        rotate_img = cv2.warpAffine(src_img,M,(src_w,src_h))

    except:
        ret = 10221
        return ret,0

    return ret,rotate_img


def func_countWhitePix(ret,src_img):
    """
    Count of the number of the white pixels function
    @param  ret                   
    @param  src_img               
    @return ret                   
    @return count                 
    """
    if ret != 0:
        return ret,0

    try:
        count = cv2.countNonZero(src_img)

    except:
        ret = 10222
        return ret,0

    return ret,count


def func_check_img_light_average(ret,src_img):
    """
    Mean brightness calculation of the image function
    @param  ret                   
    @param  src_img               
    @return ret                   
    @return light_avg_value       
    """
    if ret != 0:
        return ret,0

    light_avg_value = 0

    try:
        light_avg_value = np.average(src_img)

    except:
        ret = 10223
        return ret,0

    return ret,light_avg_value


def func_diff_img(ret,src_img1,src_img2):
    """
    Generation of the differential image between the image function
    @param  ret                   
    @param  src_img1              
    @param  src_img2              
    @return ret                   
    @return diff_img　　　 　　　　　　　　
    """
    if ret != 0:
        return ret,0

    try:
        diff_img = src_img1 - src_img2

    except:
        ret = 10224
        return ret,0

    return ret,diff_img


def func_polar2cart(ret,radius, theta, center):
    """
    Polar coordinates → X-Y coordinate system conversion function
    @param  ret                   
    @param  radius                
    @param  theta                 
    @param  center                
    @return ret                   
    @return x                     
    @return y                     
    """
    if ret != 0:
        return ret,0,0

    try:
        x = radius * np.cos(theta) + center[0]
        y = radius * np.sin(theta) + center[1]

    except:
        ret = 10225
        return ret,0,0

    return ret,x,y


def func_cart2polar(ret,point_x,point_y,center):
    """
    X-Y coordinate system → polar coordinates conversion function
    @param  ret                   
    @param  point_x               
    @param  point_y               
    @param  center                
    @return ret                   
    @return radius                
    @return theta                
    @return deg                   
    """
    if ret != 0:
        return ret,0,0,0

    try:
        radius = np.sqrt((point_x - center[0])**2 + (point_y - center[1])**2)
        theta  = np.arctan2((point_y - center[1]) , (point_x - center[0]))
        deg    = theta * 180 / np.pi

        if center[1] > point_y:
            deg = deg + 360

    except:
        ret = 10226
        return ret,0,0,0

    return ret,radius,theta,deg


def func_img2polar(ret,src_img, center, pi, final_radius, initial_radius, phase_width):
    """
    Polar coordinates development image generation function
    @param  ret                   
    @param　　ｓｒｃ_img               
    @param  center                
    @param  pi                    
    @param  final_radius          
    @param  initial_radius        
    @param  phase_width           
    @return ret                   
    @return polar_img             
    """
    if ret != 0:
        return ret,0

    try:
        x = np.linspace(0 , pi , phase_width)
        y = np.arange(initial_radius, final_radius)

        theta , R = np.meshgrid(x ,y)

        ret, Xcart, Ycart = func_polar2cart(ret, R, theta, center)

        Xcart = Xcart.astype(int)
        Ycart = Ycart.astype(int)

        if src_img.ndim == 3:
            polar_img = src_img[Ycart,Xcart,:]
            polar_img = np.reshape(polar_img,(final_radius-initial_radius,phase_width,3))
        else:
            polar_img = src_img[Ycart,Xcart]
            polar_img = np.reshape(polar_img,(final_radius-initial_radius,phase_width))

    except:
        ret = 10227
        return ret,0

    return ret,polar_img


def fit_func(parameter,x,y):
    """
    
    @param  parameter             
    @param  x                     
    @param  y                     
    @return redidual              
    """
    A = parameter[0]
    B = parameter[1]
    C = parameter[2]

    redidual = (x - A) * (x - A) + (y - B) * (y - B) - C * C

    return redidual


def func_circle_fitting(ret,src_img,start_roi_x,start_roi_y,roi_width,roi_height):
    """
    Circle approximation by the least-squares method function
    @param  ret                   
    @param  ｓｒｃ_img               
    @param  start_roi_x           
    @param  start_roi_y           
    @param  roi_width             
    @param  roi_height            
    @return ret                   
    @return center_x              
    @return center_y              
    @return radius                
    """
    if ret != 0:
        return ret,0,0,0

    try:
        # SerchPoint
        index = np.where(src_img[start_roi_y : start_roi_y + roi_height , start_roi_x : start_roi_x + roi_width] > 0)
        x = index[1];
        y = index[0];
        # InitParam
        A0 = sum(x)/len(x)
        B0 = sum(y)/len(y)
        C0 = max(x) - sum(x)/len(x)
        # SetParam
        init_parameter = [A0,B0,C0]
        # 
        result = scipy.optimize.leastsq(fit_func,init_parameter,args=(x,y))
        center_x = result[0][0]
        center_y = result[0][1]
        radius   = result[0][2]

    except:
        ret = 10228
        return ret,0,0,0

    return ret,center_x, center_y, radius


def func_draw_ellipse(ret,src_img,center,axes,angle,start_angle,end_angle,color,thickness,line_type):
    """
    Function for the partial oval drawing function
    @param  ret                   
    @param　　ｓｒｃ_img               
    @param  center                
    @param  axes                  
    @param  angle                 
    @param  start_angle           
    @param  end_angle             
    @param  color                 
    @param  thickness             
    @param  line_type             
    @return ret                   
    @return proc_img              
    """
    if ret != 0:
        return ret

    try:
        cv2.ellipse(src_img,center,axes,angle,start_angle,end_angle,color,thickness,line_type)

    except:
        ret = 10229
        return ret

    return ret


def func_bitwise_and(ret,src_img1,src_img2):
    """
    Calculation of the logical product every bit of each element function
    @param  ret                   
    @param  src_img1              
    @param  src_img2              
    @return ret                   
    @return proc_img　　　　　　 　　　　　
    """
    if ret != 0:
        return ret,0

    try:
        proc_img = cv2.bitwise_and(src_img1,src_img2)

    except:
        ret = 10230
        return ret,0

    return ret,proc_img


def func_bitwise_not(ret,src_img):
    """
    Reverse each bit of the sequence function
    @param  ret                   
    @param  src_img               
    @return ret                   
    @return proc_img              
    """
    if ret != 0:
        return ret,0

    try:
        proc_img = cv2.bitwise_not(src_img)

    except:
        ret = 10231
        return ret,0

    return ret,proc_img

						
def func_horizontal_conect_img(ret,src_img1,src_img2):
    """
    Add src_img2 to the right side of src_img1 function
    _@param  ret                  
    _@param  src_img1            
    _@param  src_img2             
    _@param  2d_ddepth            
    _@param  2d_kernel            
    _@return ret                  
    _@return edge_img             
    """
    if ret != 0:
        return ret,0

    try:
        h_con_img = np.hstack((src_img1, src_img2))

    except:
        ret = 10232
        return ret,0

    return ret,h_con_img

    
def func_get_point(ret,src_img,roi_x,roi_y,roi_width,roi_height):
    """
    Search of coordinate (x,y) function
    @param  ret                   
    _@param  src_img              
    _@param  roi_x                
    _@param  roi_y                
    _@param  roi_width            
    _@param  roi_height           
    _@return ret                  
    _@return point_x              
    _@return point_y              
    """
    if ret != 0:
        return ret,0,0

    try:
        index = np.where(src_img[roi_y : roi_y + roi_height , roi_x : roi_x + roi_width] > 0)
        point_x = roi_x + index[1];
        point_y = roi_y + index[0];

    except :
        ret = 10233
        return ret,0,0

    return ret,point_x,point_y


def func_create_zero_img(ret,src_img):
    """
    Security of the designation domain function
    @param  ret                   
    _@param  src_img              
    _@return ret                  
    _@return zero_img             
    """
    if ret != 0:
        return ret,0

    try:
        zero_img = np.zeros((src_img.shape[0],src_img.shape[1],1),np.uint8)

    except:
        ret = 10234
        return ret,0

    return ret,zero_img
    
    