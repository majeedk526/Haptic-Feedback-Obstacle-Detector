import numpy as np
import cv2
from matplotlib import pyplot as plt

def calc_disp_map(lock, stop)

    while(not stop)
        lock.acquire()
        try:    
            imgL = cv2.imread('imgL.jpg',0)
            imgR = cv2.imread('imgR.jpg',0)
            stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
            disparity = stereo.compute(imgL,imgR) # calculated disparity
            #plt.imshow(disparity,'gray')
            #plt.show()
        finally:
            lock.release()

    print('exiting disp calculations')