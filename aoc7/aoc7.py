import intcode, itertools
from numpy import loadtxt

inputProgram =  loadtxt("input.txt", delimiter=",", dtype=int)
nAmps = 5
# phaseSequences = map(lambda x:  list(x), list(itertools.permutations(range(nAmps), nAmps)))
#
# program, out = intcode.executeIntcode(inputProgram.copy(), [0,0])
#
#
# def executePhaseSequence(inputVector):
#     out = 0;
#     for _ in range(nAmps):
#         program, out = intcode.executeIntcode(inputProgram.copy(), [inputVector.pop(0),out])
#     return out
#
# outmax = max(map(executePhaseSequence, phaseSequences))
# print "OUTMAX %s" %outmax

phaseSequences = map(lambda x:  list(x), list(itertools.permutations(range(5,10), nAmps)))

def executePhaseSequenceFeedback(inputVector):
    print ("Executing Phase Sequence %s" %inputVector)
    amps = [intcode.IntcodeComputer(inputProgram.copy(), inputBuffer=[], outputBuffer=[], haltOnOutput=True) for _ in
            range(5)]
    i = 0
    lastOutput = 0;
    while not amps[0].halted:
        print ("Executing Amp %s" %(i%5))
        if inputVector:
            amps[i%5].inputBuffer.append(inputVector.pop(0))
        amps[i % 5].inputBuffer.append(lastOutput)
        amps[i % 5].execute()
        if not amps[i%5].halted:
            lastOutput = amps[i%5].outputBuffer.pop()
            i += 1
    print ("Value %s" %lastOutput)
    return lastOutput

outmax = max(map(executePhaseSequenceFeedback, phaseSequences))
print("OUTMAX %s" %outmax)

