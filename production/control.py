from gpiozero import Button
from gpiozero import RGBLED
from gpiozero import Servo
import board
import adafruit_tcs34725
from time import sleep

class Control:
    # constructor
    def __init__(self):
        self.button = Button(12)
        self.led = RGBLED(21, 20, 16)
        i2c = board.I2C()
        self.colorSensor = adafruit_tcs34725.TCS34725(i2c)

        self.doorServo = Servo(14)
        self.pushServo = Servo(15)
        self.vacuumMotor = Servo(18)
        self.chamberServo = Servo(23)

    # set the color of the rgb leds
    def setRGB(self, r, g, b):
        self.led.color = (r/255, g/255, b/255)  # rgb values must be between 0 and 1

    # MANH: read color from colorSensor
    def readColor(self):
        return colorSensor.color_rgb_bytes

    #Manh: reset all servos to the position zero
    def resetServos(self):
        self.doorServo.min()
        self.pushServo.min()
        self.chamberServo.min()

    # move the ball using the lever attached to pushServo
    def moveBall(self):
        self.pushServo.min()
        sleep(0.5)
        self.pushServo.max()
        sleep(0.5)
        self.pushServo.min()
        sleep(0.5)

    # opens the door of the sorting mechanism
    def openDoor(self):
        self.doorServo.min()
        sleep(0.5)
        self.doorServo.max()
        sleep(0.5)
        self.doorServo.min()
        sleep(0.5)

    # turn off vacuum, open the door, push the ball, turn on the vacuum
    def keepBall(self):
        self.setVacuumMotor(False) 
        self.openDoor()
        self.moveBall()
        self.setVacuumMotor(True)

    # turn off the vacuum
    def dropBall(self):
        self.setVacuumMotor(False)
        sleep(3)
        self.setVacuumMotor(True)

    # turn vacuum on/off
    def setVacuumMotor(self, on):
        if on:
            self.vacuumMotor.value = 0
        else:
            self.vacuumMotor.value = -1

    # drop the balls in the basket
    def dropSequence(self):
        self.chamberServo.min()
        sleep(0.5)
        self.chamberServo.max()
        sleep(0.5)
        self.chamberServo.min()
        sleep(0.5)

