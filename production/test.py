from control import *
from time import sleep

control = Control()

control.doorServo.value = -1
sleep(1)
control.doorServo.value = 0
sleep(1)
control.doorServo.value = 1
sleep(1)
control.doorServo.min()
