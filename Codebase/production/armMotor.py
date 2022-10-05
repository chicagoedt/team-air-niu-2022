from gpiozero import Servo
from gpiozero import LED
from time import sleep

motor = Servo(18)
blue = LED(16)

motor.value = -1

print("Plug in battery!")
for i in range(10):
    blue.on()
    print(8-i)
    sleep(0.5)
    blue.off()
    sleep(0.5)

motor.value = -0.6
sleep(1)
motor.value = -1
