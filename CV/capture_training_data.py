from picamera import PiCamera
from time import sleep
import cv2
from picamera.array import PiRGBArray

camera = PiCamera()
camera.resolution = (640, 480)

#########################################

raw_capture = PiRGBArray(camera, size=(640, 480))
control_data = (0, 0, 0, 0)

#########################################

sleep(0.3)

###########################################


for frame in camera.capture_continuous(raw_capture, format='rgb', use_video_port=True):
    image = frame.array

##################################################################

    raw_capture.truncate(0)

##################################################################
