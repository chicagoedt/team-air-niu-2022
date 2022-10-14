from control import *
from time import sleep

control = Control()
control.doorServo.min()
sleep(1)
control.doorServo.mid()
sleep(1)
control.doorServo.max()
sleep(1)
control.doorServo.min()
