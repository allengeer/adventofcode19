from numpy import loadtxt

inputProgram =  loadtxt("input.txt", delimiter=",", dtype=int)

def add(program, loc):
    program[program[loc+2]] = program[program[loc]] + program[program[loc+1]]

def multiply(program, loc):
    program[program[loc+2]] = program[program[loc]] * program[program[loc+1]]

def executeIntcode(program):
    instructionPointer = 0
    while program[instructionPointer] != 99:
        if program[instructionPointer] == 1:
            add(program, instructionPointer+1)
            instructionPointer += 4
        elif program[instructionPointer] == 2:
            multiply(program, instructionPointer+1)
            instructionPointer += 4
        else:
            print "Whoops"
    return program

for noun in range(0,99):
    for verb in range(0,99):
        # print "%s %s" %(noun, verb)
        trialProgram = inputProgram.copy()
        trialProgram[1] = noun
        trialProgram[2] = verb
        executeIntcode(trialProgram)
        if (trialProgram[0] == 19690720):
            print("%s %s  = %s  %s" %(noun, verb, trialProgram[0], (100*noun+verb)))