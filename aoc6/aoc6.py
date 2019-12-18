from numpy import loadtxt

inputProgram =  loadtxt("input.txt", dtype=str)

def parseOrbit(orbit):
    return (orbit[0:3], orbit[4:7])

orbits = map(parseOrbit, inputProgram)

uniqueBodies = set()
for x,y in orbits:
    uniqueBodies.add(x)
    uniqueBodies.add(y)
def calculateOrbits(body):
    acc = 0
    cb = body
    while cb:
        cb = filter(lambda (x, y): y == cb, orbits)
        if cb:
            cb = cb[0][0]
            acc += 1
    return acc
totalOrbits = sum(map(calculateOrbits, uniqueBodies))

def getAllOrbits(body):
    cb = body
    allOrbits = []
    while cb:
        cb = filter(lambda (x, y): y == cb, orbits)
        if cb:
            allOrbits.append(cb[0][0])
            cb = cb[0][0]
    return allOrbits

def findOrbitalTransferCount(you, santa):
    santaSpheres = getAllOrbits(santa)
    meSpheres = getAllOrbits(you)
    for orbit in meSpheres:
        if orbit in santaSpheres:
            return meSpheres.index(orbit) + santaSpheres.index(orbit)
    return -1

print findOrbitalTransferCount("YOU","SAN")

# print getAllOrbitsWithDistance("SAN")


# print totalOrbits