import numpy as np
import cv2
import os
import numpy as np
img1 = cv2.imread("analysed.png")
img2 = cv2.imread("analysed.png")
retval,res = cv2.threshold(img1, 20, 255, cv2.THRESH_BINARY)
cv2.imwrite("analysed.png",res) 
#retval,thresh = cv2.threshold(img1, 127, 255,cv2.THRESH_BINARY)
#thresh2 = cv2.threshold(img2, 127, 255,0)
#cv2.imwrite("aa.png",thresh)
#cv2.imshow('frame',img1)
#contours,hierarchy = cv2.findContours(thresh,2,1)
#ret,contours= cv2.findContours(thresh,2,1)
#cnt1 = contours[0]
#contours,hierarchy = cv2.findContours(thresh2,2,1)
#cnt2 = contours[0]
#ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
#print ret
