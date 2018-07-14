import cv2
import time
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

def send_result(frame,is_ok, led_ok, led_ng):
    if is_ok == True:
        cv2.putText(frame, "OK", (0, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imwrite("image\\"+ "OK_" + time.strftime("%Y%m%d-%Hh%Mm%Ss")+".jpg", frame)
        GPIO.output(led_ok, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(led_ok, GPIO.LOW)
        time.sleep(0.001)
    else:
        cv2.putText(frame, "NG", (0, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imwrite("image\\"+ "NG_" + time.strftime("%Y%m%d-%Hh%Mm%Ss")+".jpg", frame)
        GPIO.output(led_ng, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(led_ng, GPIO.LOW)
        time.sleep(0.001)