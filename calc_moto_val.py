import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(1000)
import time;


def calcVal(disp):
    val1 = val2= val3= val4 = 0
    tPixels = 240*320
    
    for i in range (0,240):
        for j in range (0, 320):
            val1 += disp[i][j]

    for i in range (0,240):
        for j in range (320, 640):
            val2 += disp[i][j]

    for i in range (240,480):
        for j in range (0, 320):
            val3 += disp[i][j]

    for i in range (240, 480):
        for j in range (320, 640):
            val4 += disp[i][j]
            
    val1 /= tPixels
    val2 /= tPixels
    val3 /= tPixels
    val4 /= tPixels
    print('%.2f'%val1, '%.2f'%val2, '%.2f'%val3, '%.2f'%val4)

    if(val1>-12):
        print('running motor 0')
        pwm.set_pwm(0,0,4095)
        time.sleep(2)
    else:
        pwm.set_pwm(0,0,0)

    if(val2>-12):
        print('running motor 1')
        pwm.set_pwm(1,0,4095)
        time.sleep(2)
    else:
        pwm.set_pwm(1,0,0)

    if(val3>-12):
        print('running motor 2')
        pwm.set_pwm(2,0,4095)
        time.sleep(2)
    else:
        pwm.set_pwm(2,0,0)

    if(val4>-12):
        print('running motor 3')
        pwm.set_pwm(3,0,4095)
        time.sleep(2)
    else:
        pwm.set_pwm(3,0,0)
    
    return val1, val2, val3, val4
