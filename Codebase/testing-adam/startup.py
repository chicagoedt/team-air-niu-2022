# add to /etc/rc.local:
# python3 /home/pi/github/team-air/Codebase/testing-adam/startup.py

from gpiozero import LED
from time import sleep

red = LED(16)
green = LED(20)
blue = LED(21)

red.on()
green.on()
blue.on()

sleep(2)
red.off()
green.off()
blue.off()
