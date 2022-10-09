from gpiozero import Servo
import board
import adafruit_tcs34725
from time import sleep

from colors import *
from servoControl import *

# initialize sensor and servos
i2c = board.I2C()
colorSensor = adafruit_tcs34725.TCS34725(i2c)

getBallColor(colorSensor)
sleep(100)
