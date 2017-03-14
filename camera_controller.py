#import cv2
import picamera

camera = picamera.PiCamera()

def start_capture(time_out):
    "captures images from cameras"
    camera.capture('imgL.jpg')
    camera.capture('imgR.jpg')