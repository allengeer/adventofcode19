from numpy import loadtxt
import numpy as np
from intcode import IntcodeComputer
from intcode.bots import ASCIIBot

input_program = list(loadtxt("input.txt", delimiter=",", dtype=int))
computer = IntcodeComputer(input_program, printToConsole=False, haltOnOutput=False)



routine_a = "L,12,R,8,L,6,R,8,L,6\n"
routine_b = "R,8,L,12,L,12,R,8\n"
routine_c = "L,6,R,6,L,12\n"
main_routine = "A,B,A,A,B,C,B,C,C,B\n"

computer.inputBuffer = list(map(ord, main_routine+routine_a+routine_b+routine_c+"n\n"))

computer.execute()

ascii_bot = ASCIIBot(computer.outputBuffer)

ascii_bot.print_camera_map()