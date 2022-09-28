from Codebase.production.LED import LED_disc
from time import sleep

leds = LED_disc()


def wheel(in_Pos):
    Pos = 255 - in_Pos
    if (Pos < 85):
        return [255 - Pos * 3, 0, Pos * 3]

    if (Pos < 170):
        Pos -= 85
        return [0, Pos * 3, 255 - Pos * 3]

    Pos -= 170
    return [Pos * 3, 255 - Pos * 3, 0]


while True:
    print(leds.red_pin, leds.green_pin, leds.blue_pin)
    for rand_iter in range(255):
        color = wheel(rand_iter)
        leds.update(color)
        print(color)
        sleep(10)




