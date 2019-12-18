from numpy import loadtxt
import numpy as np

line1 = loadtxt("line1.txt", dtype=str, delimiter=",", comments="#")
line2 = loadtxt("line2.txt", dtype=str, delimiter=",", comments="#")

unitVectorDict = {'R': np.array([1,0]), 'L': np.array([-1,0]), 'U': np.array([0,1]), 'D': np.array([0, -1])}
#create a list of all points a line goes through
def listOfAllPoints(line):
    pointList = []
    currentPoint = np.array([0,0])
    for directionVector in line:
        unitVector = unitVectorDict[directionVector[0]]
        for _ in range(0, int(directionVector[1:])):
            pointList.append((currentPoint+unitVector).tolist())
            currentPoint += unitVector
    return pointList

# Create a list of all intersection points
pointsOfLine1 = listOfAllPoints(line1)
pointsOfLine2 = listOfAllPoints(line2)
intersectionPoints = [point for point in pointsOfLine1 if point in pointsOfLine2]
pointsOfLine2.index(intersectionPoints[0])
pointsOfLine1.index(intersectionPoints[0])

answer = min(pointsOfLine2.index(point) + pointsOfLine1.index(point) + 2 for point in intersectionPoints)