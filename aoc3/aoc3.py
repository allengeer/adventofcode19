from numpy import loadtxt
from numpy import array, append
import matplotlib.pyplot as plt


line1 = loadtxt("line1.txt", dtype=str, delimiter=",")
line2 = loadtxt("line2.txt", dtype=str, delimiter=",")

xrange = [0,0]
yrange = [0,0]
currentPosition = array([0,0])
plotx = array([0])
ploty = array([0])
for x in line1:
    dir = x[0]
    mag = int(x[1:])
    deltaVector = array([0,0])
    if dir == 'R':
        deltaVector = array([mag, 0])
    elif dir == 'L':
        deltaVector = array([-mag, 0])
    elif dir == 'U':
        deltaVector = array([0, mag])
    elif dir == 'D':
        deltaVector = array([0, -mag])
    endPos = currentPosition + deltaVector
    plotx = append(plotx, endPos[0])
    ploty = append(ploty, endPos[1])

    currentPosition = endPos
    xrange[0] = min(currentPosition[0], xrange[0])
    xrange[1] = max(currentPosition[0], xrange[1])
    yrange[0] = min(currentPosition[1], yrange[0])
    yrange[1] = max(currentPosition[1], yrange[1])
plt.plot(plotx, ploty)
print currentPosition

currentPosition = array([0,0])
plotx = array([0])
ploty = array([0])
for x in line2:
    dir = x[0]
    mag = int(x[1:])
    deltaVector = array([0,0])
    if dir == 'R':
        deltaVector = array([mag, 0])
    elif dir == 'L':
        deltaVector = array([-mag, 0])
    elif dir == 'U':
        deltaVector = array([0, mag])
    elif dir == 'D':
        deltaVector = array([0, -mag])
    endPos = currentPosition + deltaVector
    plotx = append(plotx, endPos[0])
    ploty = append(ploty, endPos[1])

    currentPosition = endPos
    xrange[0] = min(currentPosition[0], xrange[0])
    xrange[1] = max(currentPosition[0], xrange[1])
    yrange[0] = min(currentPosition[1], yrange[0])
    yrange[1] = max(currentPosition[1], yrange[1])
plt.plot(plotx, ploty, 'r')
print currentPosition
plt.show()

print xrange  #[-2535, 8391]   [-3757, 19182]
print yrange  #[0, 19371]   [0, 8238]
print currentPosition #[ 7401 18778]   [17203  4251]

# -330, 2097