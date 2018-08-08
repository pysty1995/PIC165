import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_blue = np.array([90, 50, 50], dtype=np.uint8)
upper_blue = np.array([130, 255, 255], dtype=np.uint8)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    (h, s, v) = cv2.split(res)
    blur = cv2.medianBlur(s, 5)
    el = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    tmp = cv2.erode(blur, el, iterations=1)
    (_, tmp2) = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(tmp2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    centers = []
    radi = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 100:
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, (0, 0 , 255), 2)
            centers.append(center)
            br = cv2.boundingRect(contour)
            radi.append(br[2])
    if radi:
        cv2.imwrite("found.jpg", frame)