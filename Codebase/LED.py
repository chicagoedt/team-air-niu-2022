from rpi_ws281x import Adafruit_NeoPixel, Color
import RPi.GPIO as GPIO

# LED strip configuration:
led_count = 12        # Number of LED pixels.
led_pin = 18          # GPIO pin connected to the pixels (must support PWM!).
frequency = 800000  # LED signal frequency in hertz (usually 800khz)
dma = 10          # DMA channel to use for generating signal (try 10
led_brightness = 255  # Set to 0 for darkest and 255 for brightest

class LED:

    def __init__(self, LED_PIN = led_pin, LED_COUNT=led_count, LED_BRIGHTNESS=led_brightness,LED_FREQ=frequency,LED_DMA = dma):
        self.strip = Adafruit_NeoPixel(
            LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, False, LED_BRIGHTNESS)
        self.pin = LED_PIN
        self.count = LED_COUNT
        self.brightness = LED_BRIGHTNESS
        self.DMA = LED_DMA
        self.strip.begin()
        self.color = Color(0,0,0)

        return

    def update(self, color):
        self.color = Color(color[0], color[1], color[2])
        for i in range(self.count):
            self.strip.setPixelColor(i,self.color)
        return True

    def brightness(self, brightness):
        self.strip.setbrightness(brightness)
        return True

    def clear(self):
        self.color = Color(0, 0, 0)
        for i in range(self.count):
            self.strip.setPixelColor(i,self.color)
        return True


class LED_disc:

    def __init__(self, LED_pins=[32,33,36]):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED_pins[0], GPIO.OUT)
        GPIO.setup(LED_pins[1], GPIO.OUT)
        GPIO.setup(LED_pins[2], GPIO.OUT)

        self.red = GPIO.PWM(LED_pins[0], 0.5)
        self.red_pin = LED_pins[0]
        self.green = GPIO.PWM(LED_pins[1], 0.5)
        self.green_pin = LED_pins[1]
        self.blue = GPIO.PWM(LED_pins[2], 0.5)
        self.blue_pin = LED_pins[2]

        # self.red_pin = LED_pins[0]
        # self.red = LEDPWM(LED_pins[0])
        # self.green_pin = LED_pins[1]
        # self.green = LED(LED_pins[1])
        # self.blue_pin = LED_pins[2]
        # self.blue = LED(LED_pins[2])
        return

    def update(self, color):
        self.red.ChangeDutyCycle((color[0]/255)*100)
        self.green.ChangeDutyCycle((color[1]/255)*100)
        self.blue.ChangeDutyCycle((color[2]/255)*100)
        return True

    def clear(self):
        self.update([0,0,0])
        self.red.stop()
        self.green.stop()
        self.blue.stop()
        return True
