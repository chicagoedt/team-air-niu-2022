from control import *
from armMotor import *
from time import sleep
from sorter import *

# open file to write to
filename = input("Enter a filename (with .txt at the end): ")
f = open("color-data/" + filename, "w")
print("Your output file will be saved to Codebase/production/color-data/" + filename)

def buttonPressed():
    global buttonHasBeenPressed
    buttonHasBeenPressed = True

control = Control()

control.setRGB((0, 255, 0))
control.button.wait_for_press()
control.setRGB((0, 0, 0))

armMotor(control)

control.button.when_pressed = buttonPressed
while (True):
    global buttonHasBeenPressed
    buttonHasBeenPressed = False

    control.setRGB((255, 0, 0))
    sleep(0.5)
    control.setRGB((0, 0, 0))
    sleep(0.5)

    if buttonHasBeenPressed:
        break

runSorter(control, f)

# close the file
f.close();
