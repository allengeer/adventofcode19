import numpy as np
import math


inputProgram =  list(map(lambda x: list(x), np.loadtxt("input.txt", delimiter="\n", comments=None, dtype=str)))
height = len(inputProgram)
width = len(inputProgram[0])



class StroidMap:
    def __init__(self, asteroidMap):
        self.asteroidMap = asteroidMap
        self.baseLocation = None

    def atan2tuple(self, tup):
        return -math.atan2((tup[0]-self.baseLocation[0]), (tup[1] - self.baseLocation[1]))

    def width(self):
        return len(self.asteroidMap[0])

    def height(self):
        return len(self.asteroidMap)

    def isAsteroid(self, tuple):
        return self.asteroidMap[tuple[1]][tuple[0]] == '#'

    def isVisibleFrom(self, baseLocation: tuple, asteroidLocation: tuple):
        dy = asteroidLocation[1]-baseLocation[1]
        dx = asteroidLocation[0]-baseLocation[0]
        if dx and dy:
            slope = dy/dx
            for x in range(1,abs(dx)):
                ddx = dx/abs(dx)
                ddy = dy/abs(dy)
                newloc = (baseLocation[0]+ddx*x, baseLocation[1]+slope*ddx*x)
                if float(newloc[0]).is_integer() and float(newloc[1]).is_integer():
                    if newloc != asteroidLocation:
                        if self.isAsteroid(tuple(map(lambda x: int(x), newloc))):
                            return False
        elif dx and not dy:
            for x in range (min(asteroidLocation[0], baseLocation[0])+1, max(asteroidLocation[0], baseLocation[0])):
                if self.isAsteroid((x,asteroidLocation[1])):
                    return False
        elif dy and not dx:
            for y in range (min(asteroidLocation[1], baseLocation[1])+1, max(asteroidLocation[1], baseLocation[1])):
                if self.isAsteroid((asteroidLocation[0],y)):
                    return False
        else:
            return False
        return True

    def visibleAsteroidsFrom(self, baseLocation):
        count = 0
        for y in range(len(self.asteroidMap)):
            for x in range(len(self.asteroidMap[0])):
                if (x,y) != baseLocation and self.isAsteroid((x,y)):
                    count += int(self.isVisibleFrom(baseLocation, (x,y)))
        return count

    def bestBasePosition(self):
        bestLocation = None
        bestCount = 0
        for y in range(len(self.asteroidMap)):
            for x in range(len(self.asteroidMap[0])):
                if self.isAsteroid((x, y)):
                    if (self.visibleAsteroidsFrom((x,y)) > bestCount):
                        bestLocation = (x,y)
                        bestCount = self.visibleAsteroidsFrom((x,y))
        return bestLocation, bestCount

    def listOfAstroids(self, baseLocation):
        asteroids = []
        for y in range(len(self.asteroidMap)):
            for x in range(len(self.asteroidMap[0])):
                if self.isAsteroid((x, y)):
                    if baseLocation != (x,y):
                        asteroids.append((x, y))
        return asteroids

    def asteroidsSortedByAngleFromBase(self, baseLocation):
        self.baseLocation = baseLocation
        return sorted(self.listOfAstroids(baseLocation), key=self.atan2tuple)



asteroidMap = StroidMap(inputProgram)
baseLocation , count = asteroidMap.bestBasePosition()
print (baseLocation)
zap_order = asteroidMap.asteroidsSortedByAngleFromBase(baseLocation)
print(zap_order)
print(list(map(lambda x: asteroidMap.atan2tuple(x), zap_order)))

count = 1
while zap_order:
    to_zap = []
    for location in zap_order:
        if asteroidMap.isVisibleFrom(baseLocation, location):
            to_zap.append(location)
    for zap_location in to_zap:
        print ("Removing %s" %count, zap_location)
        count += 1
        asteroidMap.asteroidMap[zap_location[1]][zap_location[0]] = '.'
        zap_order.remove(zap_location)

