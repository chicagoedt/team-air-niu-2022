from time import sleep
from statistics import mean

# convert rgb to hue
def getHue(color_rgb):
    R = color_rgb[0] / 255
    G = color_rgb[1] / 255
    B = color_rgb[2] / 255

    new_rgb = (R, G, B)

    max = -1
    max_index = -1
    min = 256
    for i in range(3):
        if (new_rgb[i] > max):
            max = new_rgb[i]
            max_index = i
        if (new_rgb[i] < min):
            min = new_rgb[i]

    hue = -1
    if (max_index == 0):
        hue = (G-B)/(max-min)
    elif (max_index == 1):
        hue = 2.0 + (B-R)/(max-min)
    elif (max_index == 2):
        hue = 4.0 + (R-G)/(max-min)

    hue *= 60
    if hue < 0:
        hue += 360
    return hue

# get the hue and temp from the color sensor
def readColorSensor(sensor):
    hue = round(getHue(sensor.color_rgb_bytes))
    temp = round(sensor.color_temperature)
    return hue, temp

# read color 3 times, get the average, then return a string color depending on hue and temp values
def getBallColor(sensor):
    hueList = []
    tempList = []
    colorsList = []

    for i in range(3):
        print("getting average...")
        h, t = readColorSensor(sensor)
        hueList.append(h)
        tempList.append(t)
        sleep(0.3)

    hueAvg = mean(hueList)
    tempAvg = mean(tempList)

    if hueAvg >= 358 or hueAvg <= 4:
        colorsList.append("red")
    if hueAvg >= 5 and hueAvg <= 10:
        colorsList.append("orange")
    if hueAvg >= 30 and hueAvg <= 70:
        colorsList.append("yellow")
    if hueAvg >= 100 and hueAvg <= 130:
        colorsList.append("green")
    if hueAvg >= 210 and hueAvg <= 240:
        colorsList.append("blue")
    if hueAvg >= 250 and hueAvg <= 270:
        colorsList.append("purple")
    if hueAvg >= 350 or  hueAvg <= 2:
        colorsList.append("pink")


    if len(colorsList) == 0:
        return None
    elif len(colorsList) == 1:
        return colorsList[0]
    else:
        if tempAvg >= 2200 or tempAvg <= 2700:
            return "red"
        if tempAvg >= 2400 and tempAvg <= 2500:
            return "orange"
        if tempAvg >= 2400 and tempAvg <= 2900:
            return "yellow"
        if tempAvg >= 4000 and tempAvg <= 7000:
            return "green"
        if tempAvg >= 12000 and tempAvg <= 15000:
            return "blue"
        if tempAvg >= 5800 and tempAvg <= 6100:
            return "purple"
        if tempAvg >= 3600 and tempAvg <= 3800:
            return "pink"
