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

# program loop
def runSorter(control):
    # initialize the sequences
    s1 = ("blue", "purple", "red", "blue")
    seqIndex = 0

    control.resetServos()
    control.setVacuumMotor(True)

    while (seqIndex <= 3):
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

                #wait for user to decide drop the ball
                userInput = input('Enter # to drop the ball')
                while (userDec != '#'):
                    print('You enter', userInput, 'and it does nothing')
                    userDec = input('Enter # to drop the ball')

                #drop the ball from the storage chamber
                control.dropSequence() 
                seqIndex += 1

            # otherwise drop it    
            else:  
                print("dropping ball")
                control.dropBall()

        

