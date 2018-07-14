import cv2
import tkinter as tk
##fake RPi.GPIO on windows
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO
##############################
import time
from datetime import datetime
###############################
from Analyze_file import save_data
from Analyze_file import read_data
from send_result import send_result
from main_process import after_control
from camera_parameters import camera_parameters
#import picamera #// uncomment when use on RP
#import picamera.array #// uncomment when use on RP
#import cmlib
#from cmlib import piLib
###### GPIO settings
GPIO.setwarnings(False) #No warning GPIO on screen
led_control = 11
led_ok = 16
led_ng = 18
product_ok = 0
product_ng = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_control, GPIO.INPUT, pull_up_down=GPIO.PUD_UP) # led_control is always HIGH(normally case)
GPIO.setup(led_ok, GPIO.OUT)
GPIO.setup(led_ng, GPIO.OUT)
GPIO.output(led_ok, GPIO.LOW)
GPIO.output(led_ng, GPIO.LOW)
#########################
is_ok = True
text = 'NG'

now = datetime.now()
cap = cv2.VideoCapture(0)
camera_parameters(cap)
#########################
read_data()
#########################

while(True):
    is_ok = True
    key = cv2.waitKey(2)
    ret, frame1 = cap.read()
    GPIO.add_event_detect(led_control, GPIO.FALLING)
    GPIO.add_event_callback(led_control, after_control(frame1, product_ok, product_ng, key))
    if is_ok == True:
        product_ok = product_ok + 1
    else:
        product_ng = product_ng + 1
    send_result(frame1, is_ok, led_ok, led_ng)
    if key == 115: #'s' save and exit
        save_data(product_ok, product_ng)
        break
    else:
        pass
cap.release()
cv2.destroyAllWindows()
