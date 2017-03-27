import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(19, IO.OUT)
p= IO.PWM(19,100)
p.start(50)
time.sleep(2)
p.ChangeDutyCycle(40)
time.sleep(2)
p.ChangeDutyCycle(30)
time.sleep(2)
p.ChangeDutyCycle(60)
time.sleep(2)
p.ChangeDutyCycle(80)
time.sleep(2)
p.ChangeDutyCycle(0)