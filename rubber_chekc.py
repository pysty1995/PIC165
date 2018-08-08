import cv2
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
from PIL import Image
###############################
from Analyze_file import save_data
from Analyze_file import read_data
from send_result import send_result
from main_process import after_control
from camera_parameters import camera_parameters
from main_process import ROI_tracking

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
is_ok = {}

now = datetime.now()
cap = cv2.VideoCapture(0)
camera_parameters(cap)
ret, frame = cap.read()
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
r,h,c,w = 200,100,300,100
track_window = (c,r,w,h)
roi_hist = ROI_tracking(frame)
#########################
read_data()
#########################
while(True):
    key = cv2.waitKey(2)
    ret, frame1 = cap.read()
    #GPIO.add_event_detect(led_control, GPIO.FALLING)

    #GPIO.add_event_callback(led_control, after_control(frame1, product_ok, product_ng, key, track_window, roi_hist, term_crit))
    if not GPIO.input(led_control):
        after_control(frame1, product_ok, product_ng, key, track_window, roi_hist, term_crit)
    else:
        pass
    is_ok = after_control(frame1, product_ok, product_ng, key, track_window, roi_hist, term_crit)
    if is_ok == True:
        product_ok = product_ok + 1
        #time.sleep(0.5)
    else:
        product_ng = product_ng + 1
        #time.sleep(0.5)
    send_result(frame1, is_ok, led_ok, led_ng)
    print("Main " + str(is_ok))
    if key == 115: #'s' save and exit
        save_data(product_ok, product_ng)
        break

    else:
        pass
cap.release()
cv2.destroyAllWindows()
