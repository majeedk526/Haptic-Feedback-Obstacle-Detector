import cv2
import time

def start_capture(lock, stop):
    "captures images from cameras"
    config()
    count=0
    while(not stop):
        lock.acquire()
        if(count==10):
            stop = True
        else:
            count += 1
        print(('%s %d'), ('lock acquired by camera : ', count))
        try:
            ret1, frame1 = cam1.read()
            ret2, frame2 = cam2.read()
            cv2.imwrite('imgL.jpg', frame1)
            cv2.imwrite('imgR.jpg', frame2)
        finally:
            print('lock released by camera')    
            lock.release();
            time.sleep(1)

    release()
    print('stopping image capture')
    
def config():
    print('configureing camera')
    global cam1, cam2
    cam1 = cv2.VideoCapture(0)
    cam2 = cv2.VideoCapture(1)
    cam1.set(cv2.CAP_PROP_FPS,10)
    cam2.set(cv2.CAP_PROP_FPS,10)    

def release():
    print('releasing camera resource')
    cam1.release()
    cam2.release()
    cv2.destroyAllWindows()
    
def single_capture():
    config()
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()
    cv2.imwrite('imgL.jpg', frame1)
    cv2.imwrite('imgR.jpg', frame2)
    release()
