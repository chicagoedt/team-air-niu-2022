# add to /etc/rc.local:
# python3 /home/pi/github/team-air/production/startup.py

from armMotor import *
from sorter import *

def buttonPressed():
    global buttonHasBeenPressed
    buttonHasBeenPressed = True

control = Control()

control.setRGB((0, 255, 0))
control.button.wait_for_press()
control.setRGB((0, 0, 0))

armMotor(control)

control.button.when_pressed = buttonPressed
while (True):
    global buttonHasBeenPressed
    buttonHasBeenPressed = False

    control.setRGB((255, 0, 0))
    sleep(0.5)
    control.setRGB((0, 0, 0))
    sleep(0.5)

    if buttonHasBeenPressed:
        break

runSorter(control)
