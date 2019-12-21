from numpy import loadtxt
import numpy as np
inputProgram =  str(loadtxt("input.txt", dtype=str))

width = 25
height = 6
frameWidth = width*height

def countDigitsInFrame(frame, digit):
    return inputProgram[frame * frameWidth:((frame + 1) * frameWidth)].count(digit)

def countZeroesInFrame(frame):
    return countDigitsInFrame(frame, '0')

zeroCounts = map(countZeroesInFrame,range(len(inputProgram)/frameWidth))
minZerosFrame = zeroCounts.index(min(zeroCounts))

print countDigitsInFrame(minZerosFrame, '1') * countDigitsInFrame(minZerosFrame, '2')

frames = np.array_split(list(inputProgram), len(inputProgram)/frameWidth)
pixelVectors = zip(*frames)

def printPixel(pixelVector):
    for x in pixelVector:
        if x != "2":
            return ' ' if x == "0" else 'X'

for row in range(height):
    for col in range(width):
        print printPixel(list(pixelVectors[row*width + col])),
    print ''

