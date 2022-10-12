import numpy as np
from control import *
from colors import *
        
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

# program loop
def runSorter(control):
    # initialize the sequences
    s1 = ("blue", "purple", "red", "blue")
    lightColors = {
        "red":(255, 0, 0),
        "orange":(255, 165, 0),
        "yellow":(255, 255, 0),
        "green":(0, 255, 0),
        "blue":(0, 0, 255),
        "purple":(255, 0, 255),
        "pink":(255,192,203)
    }
    seqIndex = 0

    control.resetServos()
    control.setVacuumMotor(True)

    while (True):
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

                #wait for user to decide dropping the ball
                userType = input('Enter # to drop the ball')
                while(userType != '#'):
                    userType = input('Enter # to drop the ball')
                
                #drop ball
                control.dropSequence()
                seqIndex += 1
            else:  # otherwise drop it
                print("dropping ball")
                control.dropBall()


