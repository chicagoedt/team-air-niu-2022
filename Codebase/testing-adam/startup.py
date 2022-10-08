# add to /etc/rc.local:
# python3 /home/pi/github/team-air/Codebase/testing-adam/startup.py

from gpiozero import LED
from gpiozero import Button
from time import sleep

red = LED(16)
green = LED(20)
blue = LED(21)
button = Button(12)

red.on()
green.on()
blue.on()

button.wait_for_press()

red.off()
green.off()
blue.off()
