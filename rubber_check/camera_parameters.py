import cv2
def camera_parameters(cap):
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
    cap.set(cv2.CAP_PROP_CONTRAST, 25)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 25)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, True)