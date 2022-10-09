from time import sleep
import numpy as np

# these are the values we get from testing
red = (74, 5, 3)
orange = (67, 8, 2)
yellow = (27, 27, 2)
green = (8, 41, 7)
blue = (2, 18, 47)
purple = (13, 11, 27)
pink = (43, 6, 1)

colors = {
    "red":red,
    "orange":orange,
    "yellow":yellow,
    "green":green,
    "blue":blue,
    "purple":purple,
    "pink":pink
}

# find the closest vector to the color sensor reading
def getClosestColor(rgbAverage):
    minDistance = 444  # farthest possible distance is sqrt(256^2 + 256^2 + 256^2) = 443.4
    minColor = ""

    # calculate euclidean distance between each color and rgbAverage,
    # updating min as we go
    for key, value in colors.items():
        distance = np.linalg.norm(value - rgbAverage)
        if distance < minDistance:
            minDistance = distance
            minColor = key

    # return string of closest color
    return minColor
