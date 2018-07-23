import numpy as np
import cv2
from Tkinter import Tk, Frame, BOTH, Button,RIGHT,RAISED,LEFT,IntVar,BOTTOM
cap = cv2.VideoCapture(0)
startIndex = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
a=0

while(cap.isOpened()):
	ret, frame = cap.read()
	
    #ret,image2=cap.read()

	if ret==True:
		#frame = cv2.flip(frame,20)

		out.write(frame)

		cv2.imshow('frame',frame)
        #cv2.imshow('dd',image2)
		#if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.waitKey(200)	
		a=a+1	
		print(a)
		#if ( a==20):
				#cap.close()
       
        


Cap.imread(frame)
#Cap.imread(image2)
cap.release()
out.release()
cv2.destroyAllWindows()


