import numpy as np
import cv2

detector_eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
detector_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
detector_body = cv2.CascadeClassifier('haarcascade_fullbody.xml')
detector_smile = cv2.CascadeClassifier('haarcascade_smile.xml')
eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)
while (True):
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 10, 50)
    eyes = detector_eyes.detectMultiScale(gray, 1.3, 5)
    faces = detector_face.detectMultiScale(gray, 1.3, 5)
    body = detector_body.detectMultiScale(gray, 1.3, 5)
    smile = detector_smile.detectMultiScale(gray, 1.3, 5)
    glasses = eye_glass.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    for (x, y, w, h) in body:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('edged', edged)
    cv2.imshow('frame', img)
    cv2.imshow('HSV', hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()