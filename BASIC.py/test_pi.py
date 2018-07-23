import io
import time
import picamera

# Create an in-memory stream
my_stream = io.BytesIO()
picamera.PiCamera.resolution = (400,400)
with picamera.PiCamera() as camera:
	
    camera.start_preview()
    # Camera warm-up time
    time.sleep(200)
    camera.capture(my_stream, 'a.jpeg')
