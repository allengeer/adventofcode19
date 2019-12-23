from numpy import loadtxt
import numpy as np
from intcode import IntcodeComputer

input_program = list(loadtxt("input.txt", delimiter=",", dtype=int))
computer = IntcodeComputer(input_program, printToConsole=False, haltOnOutput=True)

class HullPaintingRobot:
    def __init__(self, computer: IntcodeComputer, ship_size=(100,100), robot_location=(50,50), start_white=False):
        self.ship = np.full(ship_size, '.')
        self.brain = computer
        self.location = robot_location
        self.heading = (0,-1)
        self.painted_locations = set()
        if start_white:
            self.ship[self.location[1]][self.location[0]] = '#'

    def turn_left(self):
        self.heading = (self.heading[1], -self.heading[0])

    def turn_right(self):
        self.heading = (-self.heading[1], self.heading[0])

    def move_robot(self):
        self.location = tuple(map(lambda x, y: x + y, self.location, self.heading))

    def paint_location(self, color):
        self.ship[self.location[1]][self.location[0]] = "#" if color else '.'
        self.painted_locations.add(self.location)

    def turn_and_move(self, dir):
        if dir:
            self.turn_right()
        else:
            self.turn_left()
        self.move_robot()

    def read_color(self):
        return 1 if self.ship[self.location[1]][self.location[0]] == '#' else 0

    def paint_ship(self):
        while not self.brain.halted:
            self.brain.inputBuffer.append(self.read_color())
            self.brain.execute()
            if not self.brain.halted:
                self.paint_location(self.brain.outputBuffer.pop(0))
                self.brain.execute()
                self.turn_and_move(self.brain.outputBuffer.pop(0))


bot = HullPaintingRobot(computer, start_white=True)
bot.paint_ship()


