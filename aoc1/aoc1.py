from math import floor
from numpy import loadtxt

def fuelRequired(mass):
    return floor(mass/3)-2

def totalFuelRequired(mass):
    acc = fuelRequired(mass)
    total = 0
    while acc > 0:
        total += acc
        acc = fuelRequired(acc)
    return total

moduleMasses = loadtxt("input.txt", delimiter="\n")

print sum(map(fuelRequired, moduleMasses))

print sum(map(totalFuelRequired, moduleMasses))