# add to /etc/rc.local:
# python3 /home/pi/github/team-air/Codebase/production/startup.py

from gpiozero import LED
from gpiozero import Button
from time import sleep

blue = LED(16)
green = LED(20)
red = LED(21)
button = Button(12)

green.on()

button.wait_for_press()

green.off()
