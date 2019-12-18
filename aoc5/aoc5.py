from numpy import loadtxt

inputProgram =  loadtxt("input.txt", delimiter=",", dtype=int)

def isImm(p, ptypestr):
    return ptypestr[p] == '1'

def add(program, loc, ptypestr):
    program[program[loc+2]] = (program[loc] if isImm(0,ptypestr) else program[program[loc]]) + (program[loc+1] if isImm(1,ptypestr) else program[program[loc+1]])

def multiply(program, loc, ptypestr):
    program[program[loc+2]] = (program[loc] if isImm(0,ptypestr) else program[program[loc]]) * (program[loc+1] if isImm(1,ptypestr) else program[program[loc+1]])

def inputValue(program, loc):
    x = input()
    program[program[loc]] = x

def outputValue(program, loc, ptypestr):
    print (program[loc] if isImm(0,ptypestr) else program[program[loc]])

def jumpIfTrue(program, loc, ptypestr):
    if (program[loc] if isImm(0, ptypestr) else program[program[loc]]):
        return program[loc+1] if isImm(1, ptypestr) else program[program[loc+1]]
    else:
        return loc+2

def jumpIfFalse(program, loc, ptypestr):
    if not (program[loc] if isImm(0, ptypestr) else program[program[loc]]):
        return program[loc+1] if isImm(1, ptypestr) else program[program[loc+1]]
    else:
        return loc+2

def lessThan(program, loc, ptypestr):
    program[program[loc+2]] = int((program[loc] if isImm(0, ptypestr) else program[program[loc]]) < (program[loc+1] if isImm(1, ptypestr) else program[program[loc+1]]))

def equals(program, loc, ptypestr):
    program[program[loc+2]] = int((program[loc] if isImm(0, ptypestr) else program[program[loc]]) == (program[loc+1] if isImm(1, ptypestr) else program[program[loc+1]]))

def executeIntcode(program):
    instructionPointer = 0
    while program[instructionPointer] != 99:
        instruction = program[instructionPointer] % 100
        ptypestr = ''.join(reversed(str((program[instructionPointer] - instruction)/100).zfill(3)))
        if instruction == 1:
            add(program, instructionPointer+1,ptypestr)
            instructionPointer += 4
        elif instruction == 2:
            multiply(program, instructionPointer+1,ptypestr)
            instructionPointer += 4
        elif instruction == 3:
            inputValue(program, instructionPointer+1)
            instructionPointer += 2
        elif instruction == 4:
            outputValue(program, instructionPointer+1,ptypestr)
            instructionPointer += 2
        elif instruction == 5:
            instructionPointer = jumpIfTrue(program, instructionPointer+1, ptypestr)
        elif instruction == 6:
            instructionPointer = jumpIfFalse(program, instructionPointer+1, ptypestr)
        elif instruction == 7:
            lessThan(program, instructionPointer + 1, ptypestr)
            instructionPointer += 4
        elif instruction == 8:
            equals(program, instructionPointer + 1, ptypestr)
            instructionPointer += 4
        else:
            print "Whoops"
    return program

# executeIntcode(inputProgram)

# executeIntcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])