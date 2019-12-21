from numpy import loadtxt
from intcode import IntcodeComputer

inputProgram =  list(loadtxt("input.txt", delimiter=",", dtype=int))

computer = IntcodeComputer(inputProgram)
print computer.execute().outputBuffer