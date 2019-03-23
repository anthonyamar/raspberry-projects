from picamera import PiCamera
from time import sleep
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

camera = PiCamera()
camera.rotation = 180
camera.resolution = (64, 64)

camera.start_preview()
sleep(60)
camera.capture(dir_path)
camera.stop_preview()