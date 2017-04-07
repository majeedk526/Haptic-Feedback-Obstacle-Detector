import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(1000)

def vibrate_motor(channel, start):
    pwm.set_pwm(channel,start,4095)

def stop_vibrate(channel):
    pwm.set_pwm(channel,4095,4095)
