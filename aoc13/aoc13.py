from numpy import loadtxt
import numpy as np
from arcade import Arcade

from intcode import IntcodeComputer

input_program = list(loadtxt("input.txt", delimiter=",", dtype=int))
computer = IntcodeComputer(input_program, printToConsole=False, haltOnOutput=True)
arcade = Arcade((10,10))

computer.execute()
paddle_x = ball_x = 0
while not computer.halted:
    computer.execute()
    computer.execute()
    x_coord, y_coord, tile_id = computer.outputBuffer.pop(0), computer.outputBuffer.pop(0),computer.outputBuffer.pop(0)
    arcade.write_location(x_coord,y_coord,tile_id)
    if (tile_id == 3):
        paddle_x = x_coord
    if (tile_id == 4):
        ball_x = x_coord
        if paddle_x:
            computer.inputBuffer.append(1 if ball_x > paddle_x else -1 if ball_x < paddle_x else 0)
        else:
            computer.inputBuffer.append(0)
    if (x_coord == -1):
        arcade.score = tile_id
        # print(arcade.score)
    computer.execute()


unique, counts = np.unique(arcade.screen, return_counts=True)
if 2 in unique:
    print ("Blocks: %s" %counts[2])
else:
    print ("GAME OVER: %s" %arcade.score)
print ("Done")