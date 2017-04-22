import camera_controller as cam
import disp_map as disp
import calc_moto_val as calc


def perform():
    cam.single_capture()
    d = disp.single_disp()
    v1, v2, v3, v4 = calc.calcVal(d)
    print(('%d %d %d %d'), (v1,v2,v3,v4)) 
    
