import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

def calc_disp_map(lock, stop):
    count = 0
    while(not stop):
        lock.acquire()
        if(count==10):
            stop = True
        else:
            count += 1
        print(('%s %d'), ('lock acquired by disparity ', count))
        try:    
            imgL = cv2.imread('imgL.jpg',0)
            imgR = cv2.imread('imgR.jpg',0)
            stereo = cv2.StereoBM_create(numDisparities=16, blockSize=61)
            disparity = stereo.compute(imgL,imgR) # calculated disparity
            plt.imshow(disparity,'gray')
            #plt.show()
        finally:
            lock.release()
            print('lock released by disparity')
            time.sleep(1)

    print('exiting disp calculations')

def single_disp():
    imgL = cv2.imread('imgL.jpg',cv2.IMREAD_GRAYSCALE)
    imgR = cv2.imread('imgR.jpg',cv2.IMREAD_GRAYSCALE)
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=61)
    disparity = stereo.compute(imgL,imgR) # calculated disparity
    plt.imshow(disparity,'gray')
    plt.show() 
