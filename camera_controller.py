#import cv2
import picamera
import time
#from time import time, sleep

camera = picamera.PiCamera()

def start_capture(lock, stop):
    "captures images from cameras"
    count=0
    while(not stop):
        lock.acquire()
        if(count==10):
            stop = True
        else:
            count += 1
        print(('%s %d'), ('lock acquired by camera : ', count))
        try:
            camera.capture('imgL.jpg')
            camera.capture('imgR.jpg')
        finally:
            print('lock released by camera')    
            lock.release();
            time.sleep(1)

    print('stopping image capture')
    
