from time import sleep
from control import *

if __name__ = "__main__": 
    control = Control()
    armMotor(control)

def armMotor(control):
    control.vacuumMotor.value = -1

    print("Plug in battery!")
    for i in range(10):
        control.setRGB(0, 0, 255)
        print(10-i)
        sleep(0.5)
        control.setRGB(0, 0, 0)
        sleep(0.5)

    control.vacuumMotor.value = -0.6
    sleep(1)
    control.vacuumMotor.value = -1
