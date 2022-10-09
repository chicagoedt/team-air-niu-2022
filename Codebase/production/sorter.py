import numpy as np

from colors import *

# initialize the sequences
s1 = ("blue", "purple", "red", "blue")
s2 = ("green", "yellow", "red", "green")
s3 = ("blue", "purple", "red", "green")
sequence = (s1, s2, s3)
seqIndex = 0


# set this to the "ambient" chamber rgb reading of the color sensor
ambientColor = (67, 10, 3)
# (255, 0, 0)
# (45, 0, 0)

# caleb's attempt to boost the color, use 1.4 as a ratio
def boostColor(rgbValues):
    r = int(rgbValues[0] * 1.4)
    g = int(rgbValues[1] * 1.4)
    b = int(rgbValues[2] * 1.4)
    return (r, g, b)

# determine if ball is in the chamber (sensor color a certain distance from ambient color)
def ballInChamber(sensorRGB):
    if (sensorRGB == (45, 0, 0) or sensorRGB == (255, 0, 0)):
        print('no ball')
        return False
    print('ball')
    return True

    # distance = np.linalg.norm(np.array(sensorRGB) - ambientColor)
    # print(distance)
    # return distance > 20 # return true if color is within some distance
    # return True

# read color 10 times, get the average, then return a string color closest to that average
def getBallColor(control):
    rgbReadings = []
    numReadings = 10

    print("getting average...")

    for i in range(numReadings):
        rgbReadings.append(control.readColor())
        sleep(0.1)

    rgbAverage = np.mean(rgbReadings, 0)

    print("sd:", np.std(rgbReadings, 0))
    print("avg:", rgbAverage)

    return getClosestColor(rgbAverage)

def runSorter(control):
    control.resetServos()
    control.setVacuumMotor(True)

    while (True):
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

