import threading
import camera_controller as camCont
import disp_map
from time import time, sleep

def main():

    lock = threading.Lock()
    stop = False
    camCont.start_capture(lock, stop)
    disp_map.calc_disp_map(lock, stop)

    while(not stop):
        ip = input('Type s to stop')
        if(ip == 's'):
            stop = True        

    print('exiting main thread')


if(__name__ == '__main__'):
    main()