# add to /etc/rc.local:
# python3 /home/pi/github/team-air/production/startup.py

from armMotor import armMotor
from control import Control

control = Control()

control.setRGB(0, 255, 0)
control.button.wait_for_press()
control.setRGB(0, 0, 0)

armMotor(control)
