from picamera import PiCamera
from time import sleep
import cv2
from picamera.array import PiRGBArray

camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation=180
raw_capture = PiRGBArray(camera, size=(640, 480))


sleep(0.3)


for frame in camera.capture_continuous(raw_capture, format='rgb', use_video_port=True):
    image = frame.array

    screen = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow('Frame', screen)
    key = cv2.waitKey(1)

    raw_capture.truncate(0)

    if key == ord('q'):
        break
