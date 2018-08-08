from typing import Any, Union

from imutils import paths
import cv2
import numpy as np
import imutils
import datetime
import math
#def distance calculator
def distance_to_camera(knowWidth, focalLength, perWidth):
    return (knowWidth * focalLength) / perWidth
#def color
black = (0, 0, 0)
green = (0, 255, 0)
blue = (255, 0, 0)
red = (0, 0, 255)
lime = (161, 166, 255)
orange = (0, 166, 255)
yellow = (0, 255, 255)
violet = (255, 131, 188)
white = (255, 255, 255)
#def const-var
font = cv2.FONT_HERSHEY_SIMPLEX
KNOWN_DISTANCE = 24.0
KNOWN_WIDTH = 11.0
#def object
img = cv2.imread("dt.jpg")
roi = img[252: 395, 354: 455]
x = 354
y = 252
width = 455 - x
height = 395 - y
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
#read from webcam
cap = cv2.VideoCapture(0)
#define output video type
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
#while loop
while True:
    frame, frame = cap.read()
# object follower
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    ret, track_window = cv2.CamShift(mask, (x, y, width, height), term_criteria)
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.drawContours(frame, [pts], -1, white, 2)
#distance measurement
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray_gaussian, 35, 125)
    contour = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contour, -1, green, 1)
    contour = contour[0] if imutils.is_cv2() else contour[1]
    c = max(contour, key=cv2.contourArea)
    marker = cv2.minAreaRect(c )
#done matching contour
    box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
    box = np.int0(box)
    cv2.drawContours(frame, [box], -1, blue, 2)
    num = marker[1][0]
    focalLength = (num * KNOWN_DISTANCE) / KNOWN_WIDTH
    inches = (KNOWN_WIDTH*focalLength/num)*2.54
    cv2.putText(frame, "%.2fcm" % inches, (frame.shape[1] - 200, frame.shape[0] - 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, green, 2)
    cv2.putText(frame, "FocalLen:%.2f" % focalLength, (frame.shape[1] - 300, frame.shape[0]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, violet, 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, orange, 2)
#done measure and show result
#write output.avi
    video = cv2.flip(frame, 1) #1:non-reversed
    out.write(video)
#done writing
    #cv2.imshow("mask", mask)
    cv2.imshow("Frame", frame)
    cv2.imshow("Canny", edged)
    cv2.imshow("Gaussian", gray_gaussian)
    key = cv2.waitKey(1)
    if key == 32: # press space to capture img
        cv2.imwrite('frame.jpg', frame)
    if key == 13: #press enter to close recording video
        out.release()
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
