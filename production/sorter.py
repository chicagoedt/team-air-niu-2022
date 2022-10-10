import numpy as np
from colors import *

# boost color by 40%
def boostColor(rgbValues):
    r = int(rgbValues[0] * 1.4)
    g = int(rgbValues[1] * 1.4)
    b = int(rgbValues[2] * 1.4)
    # cap r,g,b values at 255  
    #MANH: I dont like this: if all rgb values after boosted are > 255 then we boostColor to a totally different color
    #MANH: A better solution is that we should find max among r, g, b after being boosted. If that max is greated than 255,
    #MANH: set that max to 255 and the other is ratio respective of the max (This may be annoying)
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    return (r, g, b)

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

    print("std:", np.std(rgbReadings, 0)) #MANH: I just fix from 'sd' to 'std'
    print("avg:", rgbAverage)

    return getClosestColor(rgbAverage)

# program loop
def runSorter(control):
    # initialize the sequences
    s1 = ("blue", "purple", "red", "blue")
    s2 = ("green", "yellow", "red", "green")
    s3 = ("blue", "purple", "red", "green")
    sequence = (s1, s2, s3)
    seqIndex = 0

    control.resetServos() #MANH: curious, do u need to import control.py to have access to class control?
    control.setVacuumMotor(True) 

    while (True): #MANH: this while loop just never end ???, we need to make this while loop more controllable
        sensorRGB = control.readColor()

        # ball in the chamber
        if ballInChamber(sensorRGB):
            # get color of ball as a string
            ballColor = getBallColor(control)
            print(ballColor)

            # if it matches the next color we need, keep it
            if ballColor == s1[seqIndex]:
                print("keeping ball")
                control.keepBall()
                seqIndex += 1
            else:  # otherwise drop it
                print("dropping ball")
                control.dropBall()

        # reached end of specified sequence
        if seqIndex == len(s1):
            control.dropSequence()

