import numpy as np
import cv2
from Tkinter import *
root = Tk()
Label(root,text="output").pack()


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
#GPIO.setwarnings(False)
#while True:
  #GPIO.output(14,GPIO.HIGH) #digitalWrite(18, HIGH)
  #time.sleep(1) #delay 1s
  #GPIO.output(14, GPIO.LOW) #digitalWrite(18, LOW)
  #time.sleep(1) #delay 1s

img = cv2.imread("src.png",cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(200,300),(255,255,255),50)
cv2.rectangle(img,(50,250),(100,500),(255,0,0),15)
cv2.circle(img,(447,63), 63, (0,255,0), -1)
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(img,'OpenCV Tuts!',(100,100), font, 6, (200,255,155), 13, cv2.LINE_AA)
cv2.putText(img,'OpenCV Tuts!',(100,100), font, 2, (200,255,155), 1)

#while True:
#  GPIO.output(14,GPIO.HIGH) #digitalWrite(18, HIGH)
#  time.sleep(1) #delay 1s
#  GPIO.output(14, GPIO.LOW) #digitalWrite(18, LOW)
#  time.sleep(1) #delay 1s

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

while True:
  GPIO.output(14,GPIO.HIGH) #digitalWrite(18, HIGH)
  time.sleep(1) #delay 1s
  GPIO.output(14, GPIO.LOW) #digitalWrite(18, LOW)
  time.sleep(1) #delay 1s
root.mainloop()
