import numpy as np
from control import *
from colors import *

# boost color with the ratio that would not squash the values.
def boostColor(rgbValues):
    r = int(rgbValues[0])
    g = int(rgbValues[1])
    b = int(rgbValues[2])

    rgbList = [r,g,b]
    max_value = max(rgbList)
    ratio = 255/max_value

    r = int(ratio * r)
    g = int(ratio * g)
    b = int(ratio * b)
    return (r,g,b)

# determine if ball is in the chamber
def ballInChamber(sensorRGB):
    if (sensorRGB == (45, 0, 0) or sensorRGB == (255, 0, 0)):
        print('no ball')
        return False
    print('ball')
    return True

# read color 10 times, get the average, then return a string color closest to that average
def getBallColor(control):
    rgbReadings = []
    numReadings = 10

    print("getting average...")

    for i in range(numReadings):
        rgbReadings.append(control.readColor())
        sleep(0.1)

    rgbAverage = np.mean(rgbReadings, 0)

    print("std:", np.std(rgbReadings, 0))
    print("avg:", rgbAverage)

    return getClosestColor(rgbAverage)

def buttonPressed():
    global buttonHasBeenPressed
    buttonHasBeenPressed = True

# program loop
def runSorter(control):
    # initialize the sequences
    s1 = ("blue", "purple", "red", "blue")
    s2 = ("green", "yellow", "red", "green")
    s3 = ("blue", "purple", "red", "green")
    lightColors = {
        "red":(255, 0, 0),
        "orange":(255, 40, 0),
        "yellow":(255, 150, 0),
        "green":(0, 255, 0),
        "blue":(0, 0, 255),
        "purple":(80, 0, 255),
        "pink":(255, 50, 50)
    }
    sequence = (s1, s2, s3)
    seqIndex = 0

    control.resetServos()
    control.setVacuumMotor(True)

    control.button.when_pressed = buttonPressed
    while (True):
        global buttonHasBeenPressed
        buttonHasBeenPressed = False
        sensorRGB = control.readColor()

        # ball in the chamber
        if ballInChamber(sensorRGB):
            # get color of ball as a string
            ballColor = getBallColor(control)
            print(ballColor)
            control.setRGB(lightColors[ballColor])


            # if it matches the next color we need, keep it
            if ballColor == s1[seqIndex]:
                print("keeping ball")
                control.keepBall()
                seqIndex += 1
            else:  # otherwise drop it
                print("dropping ball")
                control.dropBall()
            control.setRGB((0,0,0))

        # reached end of specified sequence
        if seqIndex == len(s1):
            control.dropSequence()

        if buttonHasBeenPressed:
            break

