import cv2
from matplotlib import pyplot as plt
import time
import calc_moto_val as calc

def calc_disp_map(lock, stop, finalCount):
    count = 0
    while(not stop):
        lock.acquire()
        if(count==finalCount):
            stop = True
        else:
            count += 1
        try:    
            imgL = cv2.imread('imgL.jpg',0)
            imgR = cv2.imread('imgR.jpg',0)
            stereo = cv2.StereoBM_create(numDisparities=16, blockSize=31)
            disparity = stereo.compute(imgL,imgR) # calculated disparity
            #plt.imshow(disparity,'gray')
            #plt.show()
            v1, v2, v3, v4 = calc.calcVal(disparity)
            #print('%.2f'%v1, '%.2f'%v2, '%.2f'%v3, '%.2f'%v4) 
        finally:
            lock.release()
            #print('lock released by disparity')
            time.sleep(1)

    print('exiting disp calculations')

def single_disp(imgL, imgR):
    imgL = cv2.cvtColor(imgL,cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
    stereo = cv2.StereoBM_create(numDisparities=8, blockSize=17)
    disparity = stereo.compute(imgL,imgR) # calculated disparity
    v1, v2, v3, v4 = calc.calcVal(disparity)
    #cv2.imshow('disp', disparity)
    #cv2.waitKey(1)
    plt.imshow(disparity,'gray')
    plt.show('dmap')
    #cv2.destroyAllWindows()
    return disparity
