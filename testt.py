import cv2
import time
from datetime import datetime
import numpy as np
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

i = 0
j = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
control_signal = 11
result_signal = 12
GPIO.setup(control_signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(result_signal, GPIO.OUT)
GPIO.output(result_signal, GPIO.LOW)

cap = cv2.VideoCapture(0)
cv2.CAP_PROP_FRAME_HEIGHT = 1024
cv2.CAP_PROP_FRAME_WIDTH = 768

image_location = 'capture.jpg'
file = open('specs.txt', 'r')
log = open('log.txt', 'r+')

lines = file.readlines()
line1 = lines[0] # start_col
line2 = lines[1] # start_row
line3 = lines[2] # end_col
line4 = lines[3] # end_row
line5 = lines[4] # threshold
line6 = lines[5] # lower_h
line7 = lines[6] # lower_s
line8 = lines[7] # lower_v
line9 = lines[8] # upper_h
line10 = lines[9] # upper_s
line11 = lines[10] # upper_v

start_col = int(line1[12] + line1[13] + line1[14])
start_row = int(line2[12] + line2[13] + line2[14])
end_col = int(line3[12] + line3[13] + line3[14])
end_row = int(line4[12] + line4[13] + line4[14])
threshold = int(line5[12] + line5[13] + line5[14])
lower_h = int( line6[12] + line6[13] + line6[14])
lower_s = int( line7[12] + line7[13] + line7[14])
lower_v = int( line8[12] + line8[13] + line8[14])
upper_h = int( line9[12] + line9[13] + line9[14])
upper_s = int( line10[12] + line10[13] + line10[14])
upper_v = int( line11[12] + line11[13] + line11[14])

print(lines)
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)
print(line9)
print(line10)
print(line11)

print("\n"+ str(start_col))
print("\n"+ str(start_row))
print("\n"+ str(end_col))
print("\n" + str(end_row))
print("\n" + str(threshold))
print("\n" + str(lower_h))
print("\n" + str(lower_s))
print("\n" + str(lower_v))
print("\n" + str(upper_h))
print("\n" + str(upper_s))
print("\n" + str(upper_v))

lower = np.array([lower_h, lower_s, lower_v])
upper = np.array([upper_h, upper_s, upper_v])

if not cap.isOpened():
    print("Camera Error!")
    log.write("\n camera init error!")
def read_signal(channel):
    if not GPIO.input(channel):
        print(GPIO.input(channel))
        frame, frame =cap.read()
        cv2.imwrite(image_location, frame)

        return True
    else:
        return False
def image_process(image_location):
        img = cv2.imread(image_location, cv2.IMREAD_COLOR)
        crop_img = img[start_row:end_row, start_col:end_col]
        hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
        height, width = hsv.shape[:2]
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(crop_img, crop_img, mask=mask)
        h = cv2.split(hsv)[0]
        s = cv2.split(hsv)[1]
        v = cv2.split(hsv)[2]
        cv2.imshow("Mask", mask)
        cv2.imshow("Crop_IMG", crop_img)
        cv2.imshow("Result", res)
while(cap.isOpened()):
    if read_signal(control_signal):
        image_process(image_location)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()