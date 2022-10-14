from control import *
from time import sleep

control = Control()
control.pushServo.min()
sleep(1)
control.pushServo.value = 0.6
sleep(1)
control.pushServo.min()
sleep(1)
control.pushServo.value = 0.6
sleep(1)
control.pushServo.min()
sleep(1)
control.pushServo.min()

