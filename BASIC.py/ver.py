import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
	#ret, frame = cap.read()
    im = cv2.imread('new.png')
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    #res = cv2.bitwise_and(im,im, mask= mask)

    cv2.imshow('frame',im)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
