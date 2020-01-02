def isImm(p, ptypestr):
    return ptypestr[p] == '1'

def isRelative(p, ptypestr):
    return ptypestr[p] == '2'

def getParameter(computer, pNum):
    if isImm(pNum, computer.ptypestr):
        return computer.program[computer.instructionPointer + 1 + pNum]
    elif isRelative(pNum, computer.ptypestr):
        return computer.program[computer.program[computer.instructionPointer + 1 + pNum] + computer.relativeBase]
    else:
        return computer.program[computer.program[computer.instructionPointer + 1 + pNum]]

def add(computer):
    if isRelative(2, computer.ptypestr):
        computer.program[computer.program[computer.instructionPointer + 3] + computer.relativeBase] = getParameter(computer, 0) + getParameter(computer, 1)
    else:
        computer.program[computer.program[computer.instructionPointer + 3]] = getParameter(computer, 0) + getParameter(computer, 1)

def multiply(computer):
    if isRelative(2, computer.ptypestr):
        computer.program[computer.program[computer.instructionPointer + 3] + computer.relativeBase] = getParameter(computer, 0) * getParameter(computer, 1)
    else:
        computer.program[computer.program[computer.instructionPointer + 3]] = getParameter(computer, 0) * getParameter(computer, 1)

def inputValue(computer):
    if isRelative(0, computer.ptypestr):
        computer.program[computer.program[computer.instructionPointer + 1] + computer.relativeBase] = computer.inputBuffer.pop(0) if computer.inputBuffer else int(input())
    else:
        computer.program[computer.program[computer.instructionPointer + 1]] = computer.inputBuffer.pop(0) if computer.inputBuffer else int(input())

def outputValue(computer):
    val = getParameter(computer, 0)
    if computer.printToConsole: print(val)
    return val

def jumpIfTrue(computer):
    if getParameter(computer, 0):
        return getParameter(computer, 1)
    else:
        return computer.instructionPointer + 3

def jumpIfFalse(computer):
    if not getParameter(computer, 0):
        return getParameter(computer, 1)
    else:
        return computer.instructionPointer + 3

def lessThan(computer):
    if isRelative(2, computer.ptypestr):
        computer.program[computer.program[computer.instructionPointer + 3] + computer.relativeBase] = int(getParameter(computer, 0) < getParameter(computer, 1))
    else:
        computer.program[computer.program[computer.instructionPointer + 3]] = int(getParameter(computer, 0) < getParameter(computer, 1))

def equals(computer):
    if isRelative(2, computer.ptypestr):
        computer.program[computer.program[computer.instructionPointer + 3] + computer.relativeBase] = int(getParameter(computer, 0) == getParameter(computer, 1))
    else:
        computer.program[computer.program[computer.instructionPointer + 3]] = int(getParameter(computer, 0) == getParameter(computer, 1))

def modifyRelativeBase(computer):
    computer.relativeBase += getParameter(computer, 0)


class IntcodeComputer:
    def __init__(self, program, inputBuffer = None, outputBuffer = None, haltOnOutput = False, printToConsole=False):
        self.program = program + [0] * 5000
        self.instructionPointer = 0
        self.inputBuffer = inputBuffer if inputBuffer else []
        self.outputBuffer = outputBuffer if outputBuffer else []
        self.haltOnOutput = haltOnOutput
        self.halted = False
        self.relativeBase = 0
        self.ptypestr = ""
        self.printToConsole = printToConsole

    def getProgram(self, trimZeros=True):
        myCopy = self.program[:]
        if trimZeros:
            for i in reversed(range(len(myCopy))):
                if myCopy[i]:
                    break
                else:
                    del myCopy[i]
        return myCopy

    def execute(self):
        while self.program[self.instructionPointer] != 99:
            instruction = self.program[self.instructionPointer] % 100
            self.ptypestr = ''.join(reversed(str(int((self.program[self.instructionPointer] - instruction) / 100)).zfill(3)))
            if instruction == 1:
                add(self)
                self.instructionPointer += 4
            elif instruction == 2:
                multiply(self)
                self.instructionPointer += 4
            elif instruction == 3:
                inputValue(self)
                self.instructionPointer += 2
            elif instruction == 4:
                self.outputBuffer.append(outputValue(self))
                self.instructionPointer += 2
                if self.haltOnOutput:
                    return;
            elif instruction == 5:
                self.instructionPointer = jumpIfTrue(self)
            elif instruction == 6:
                self.instructionPointer = jumpIfFalse(self)
            elif instruction == 7:
                lessThan(self)
                self.instructionPointer += 4
            elif instruction == 8:
                equals(self)
                self.instructionPointer += 4
            elif instruction == 9:
                modifyRelativeBase(self)
                self.instructionPointer += 2
            else:
                print ("Improper Instruction %s at Location" %instruction, self.instructionPointer)
                self.halted = True
                return
        self.halted = True
        return self


