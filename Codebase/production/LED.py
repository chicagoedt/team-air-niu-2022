# from _rpi_ws281x import Adafruit_NeoPixel, Color
import RPi.GPIO as GPIO
import board
import pwmio

# LED strip configuration:
led_count = 12  # Number of LED pixels.
led_pin = 18  # GPIO pin connected to the pixels (must support PWM!).
frequency = 800000  # LED signal frequency in hertz (usually 800khz)
dma = 10  # DMA channel to use for generating signal (try 10
led_brightness = 255  # Set to 0 for darkest and 255 for brightest


# Discrete LED pinout
# R = pin GPIO 12
# G = pin GPIO 13
# B = pin GPIO 16
# GND = the pin between pin 12 & 16
# look at testing-advik for pinout of a discrete LED

"""
how to use the LED class:
    from LED import LED_disc, LED
    variable = LED_disc() # you can pass in pin numbers for LED_disc like LED_disc([32,33,36])
    # mind you these are the board pin numbers. Use pinout.xyz to find the exact numbers
    variable.update([R,G,B]) # R G B are integers between 0-255 for the value of said Led
    variable.clear() # turns the LED off
"""
# class LED:
#
#     def __init__(self, LED_PIN=led_pin, LED_COUNT=led_count, LED_BRIGHTNESS=led_brightness, LED_FREQ=frequency,
#                  LED_DMA=dma):
#         self.strip = Adafruit_NeoPixel(
#             LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, False, LED_BRIGHTNESS)
#         self.pin = LED_PIN
#         self.count = LED_COUNT
#         self.brightness = LED_BRIGHTNESS
#         self.DMA = LED_DMA
#         self.strip.begin()
#         self.color = Color(0, 0, 0)
#
#         return
#
#     def update(self, color):
#         self.color = Color(color[0], color[1], color[2])
#         for i in range(self.count):
#             self.strip.setPixelColor(i, self.color)
#         return True
#
#     def brightness(self, brightness):
#         self.strip.setbrightness(brightness)
#         return True
#
#     def clear(self):
#         self.color = Color(0, 0, 0)
#         for i in range(self.count):
#             self.strip.setPixelColor(i, self.color)
#         return True


class LED_disc:

    def __init__(self, LED_pins=[32, 33, 36]):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED_pins[0], GPIO.OUT)
        GPIO.setup(LED_pins[1], GPIO.OUT)
        GPIO.setup(LED_pins[2], GPIO.OUT)

        self.red = GPIO.PWM(LED_pins[0], 50)
        self.green = GPIO.PWM(LED_pins[1], 50)
        self.blue = GPIO.PWM(LED_pins[2], 50)

        self.red.start(0)
        self.green.start(0)
        self.blue.start(0)
        # self.red_pin = LED_pins[0]
        # self.red = LEDPWM(LED_pins[0])
        # self.green_pin = LED_pins[1]
        # self.green = LED(LED_pins[1])
        # self.blue_pin = LED_pins[2]
        # self.blue = LED(LED_pins[2])
        return

    def update(self, color):
        self.red.ChangeDutyCycle((color[0] / 255) * 100)
        self.green.ChangeDutyCycle((color[1] / 255) * 100)
        self.blue.ChangeDutyCycle((color[2] / 255) * 100)

    def clear(self):
        self.update([0, 0, 0])
        self.red.stop()
        self.green.stop()
        self.blue.stop()
        return True

class LED_disc_CP:

    def __init__(self, LED_pins=[board.D12, board.D13, board.D16]):
        self.red = pwmio.PWMOut(LED_pins[0], frequency=5000, duty_cycle=0)
        self.green = pwmio.PWMOut(LED_pins[1], frequency=5000, duty_cycle=0)
        self.blue = pwmio.PWMOut(LED_pins[2], frequency=5000, duty_cycle=0)
        # self.red_pin = LED_pins[0]
        # self.red = LEDPWM(LED_pins[0])
        # self.green_pin = LED_pins[1]
        # self.green = LED(LED_pins[1])
        # self.blue_pin = LED_pins[2]
        # self.blue = LED(LED_pins[2])
        return

    def update(self, color):
        self.red.duty_cycle = int(color[0] * 2 * 65535 / 100)
        self.green.duty_cycle = int(color[1] * 2 * 65535 / 100)
        self.blue.duty_cycle = int(color[2] * 2 * 65535 / 100)

    def clear(self):
        self.update([0, 0, 0])
        return True
