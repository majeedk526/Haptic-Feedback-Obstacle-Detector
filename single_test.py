import camera_controller as cam
import disp_map as disp
#import calc_moto_val as calc


def perform():
    imgL, imgR = cam.single_capture()
    d = disp.single_disp(imgL, imgR)
    #v1, v2, v3, v4 = calc.calcVal(d)
    #print('%.2f'%v1, '%.2f'%v2, '%.2f'%v3, '%.2f'%v4) 
    
