from numpy import loadtxt
import numpy as np

from intcode import IntcodeComputer
from intcode import RepairBot

input_program = list(loadtxt("input.txt", delimiter=",", dtype=int))
computer = IntcodeComputer(input_program, printToConsole=False, haltOnOutput=True)
repair_bot = RepairBot(computer, ship_size=(100,100), robot_location=(50,50))

repair_bot.find_oxygen_tank()
repair_bot.cost = np.full(repair_bot.ship_size, 10000)
repair_bot.create_distance_matrix()
print("Cost To Travel to Oxygen Tank: %s" %repair_bot.cost[repair_bot.oxygen_location[1]][repair_bot.oxygen_location[0]])

repair_bot.cost = np.full(repair_bot.ship_size, 10000)
repair_bot.create_distance_matrix(location=repair_bot.oxygen_location)

print("Time to Oxy it all: %s" %np.amax(np.vectorize(lambda x: 0 if x == 10000 else x)(repair_bot.cost)))
