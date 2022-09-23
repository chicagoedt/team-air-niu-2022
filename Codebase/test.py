from Codebase.LED import LED
import numpy as np

leds = LED()


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
    for rand_iter in range(255):
        color = wheel(rand_iter)
        leds.update(color)
        print(color)




