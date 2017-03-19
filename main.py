import threading
import camera_controller as camCont
import disp_map
import time
import _thread

def main():

    lock = threading.Lock()
    stop = False
    _thread.start_new_thread(camCont.start_capture,(lock, stop))
    time.sleep(1)
    _thread.start_new_thread(disp_map.calc_disp_map,(lock, stop))

   # while(not stop):
    #    ip = input('Type s to stop')
     #   if(ip == 's'):
      #      stop = True        

    print('exiting main thread')


if(__name__ == '__main__'):
    main()
