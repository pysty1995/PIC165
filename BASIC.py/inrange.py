import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

	# Take each frame
	#ret, frame = cap.read()
	im = cv2.imread('src.png')
	#hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
	lower_green = np.array([0,0,10],np.uint8)
	upper_green = np.array([50,50,90],np.uint8)
	mask = cv2.inRange(im, lower_green, upper_green)
	res = cv2.bitwise_and(im,im, mask= mask)
	
	cv2.imshow('frame',im)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
	  break

cv2.destroyAllWindows()
