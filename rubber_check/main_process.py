import cv2
from crop_image import image_crop
from datetime import datetime
import numpy as np
from colors import *
def after_control(frame, product_ok, product_ng, key):
    print("Start to take img")
    frame1 = frame.copy()
    frame2 = image_crop(frame1)
    laplacian = cv2.Laplacian(frame2, cv2.CV_32F)
    print('Laplacian done!')
    hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gaussian, 10, 100)
    hist = cv2.calcHist([frame2], [0], None, [256], [0, 256])
    thr = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 5, 1)
    ret, thresh = cv2.threshold(frame2, 127, 255, cv2.THRESH_BINARY)

    sobel = cv2.Sobel(frame2, cv2.CV_8U, 1, 0, ksize=5)
    abs_sobel164f = np.absolute(sobel)
    sobel_8u = np.uint8(abs_sobel164f)
    cv2.putText(frame2, "OK:%d" % product_ok, (0, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.5, blue, 1)
    cv2.putText(frame2, "NG:%d" % product_ng, (0, 330), cv2.FONT_HERSHEY_SIMPLEX, 0.5, green, 1)
    cv2.putText(frame2, datetime.now().strftime("%A,%d %B %Y_%I:%M:%S%p"), (0, 370), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (255, 0, 0), 1)
    medianBlur = cv2.medianBlur(frame2, 5)
    median_hsv = cv2.cvtColor(medianBlur, cv2.COLOR_BGR2HSV)
    cv2.imshow("Image", frame2)
    #cv2.imshow("Gaussian Blur", thr)
    #cv2.imshow("Laplacian", laplacian)
    #cv2.imshow("HSV", hsv)
    #cv2.imshow("sobel", sobel_8u)

