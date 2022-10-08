from gpiozero import Button
from gpiozero import LED
from gpiozero import Servo
import board
import adafruit_tcs34725
import numpy as np
from time import sleep

from colors import *
from servoControl import *



class control:
    def __init__(self, button, doorServo, pushServo, vacuumMotor, chamberServo):
        self.button = Button(12)
        self.doorServo = Servo(14)
        self.pushServo = Servo(15)


    def moveBall(self):
        self.pushServo.min()
        sleep(0.5)
        self.pushServo.max()
        sleep(0.5)
        self.pushServo.min()
        sleep(0.5)

class rbgLED:
    def __init__(self, blue, red, green):
        self.blue = LED(16)
        self.red = LED(20)
        self.red = LED(21)








