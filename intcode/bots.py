import numpy as np
from intcode import IntcodeComputer
import matplotlib.pyplot as plt

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


class RepairBot:
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4
    HIT_WALL = 0
    MOVE_SUCCESS = 1
    OXYGEN_TANK_FOUND = 2
    UNEXPLORED = "?"
    WALL = "#"
    EMPTY = "."
    OXYGEN_TANK = "O"
    def __init__(self, computer: IntcodeComputer, ship_size=(100,100), robot_location=(50,50)):
        self.ship_size = ship_size
        self.ship = np.full(ship_size, self.UNEXPLORED)
        self.cost = np.full(ship_size, 10000)
        self.brain = computer
        self.location = robot_location
        self.start_location = robot_location
        self.oxygen_location = None
        self.ship[robot_location[0]][robot_location[1]] = self.EMPTY

    def value_at(self, location):
        return self.ship[location[1]][location[0]]

    def adjacent_locations(self, location=None):
        if not location: location = self.location
        return [(location[0]-1, location[1]), (location[0]+1, location[1]), (location[0], location[1]-1), (location[0], location[1]+1)]

    def location_to_direction(self, location):
        if (self.location[0] == location[0]):
            return self.SOUTH if location[1] > self.location[1] else self.NORTH
        elif (self.location[1] == location[1]):
            return self.EAST if location[0] > self.location[0] else self.WEST

    def move_robot(self, direction):
        self.brain.inputBuffer.append(direction)

    def print_ship(self):
        self.ship[self.start_location[1]][self.start_location[0]] = "X"
        to_print = "\n".join(["".join(row) for row in self.ship])
        print(to_print)
        self.ship[self.start_location[1]][self.start_location[0]] = self.EMPTY

    def create_distance_matrix(self, location=None, cost=0, initial_cost=10000):
        if not location: location = self.start_location
        if self.cost[location[1]][location[0]] > cost:
            self.cost[location[1]][location[0]] = cost
            list_of_points_to_update = list(filter(lambda x: self.value_at(x) == self.EMPTY or self.value_at(x) == self.OXYGEN_TANK, self.adjacent_locations(location)))
            for point_to_update in list_of_points_to_update:
                self.create_distance_matrix(point_to_update, cost+1)


    def find_oxygen_tank(self, return_to=None):
        list_of_unexplored_points = list(filter(lambda x: self.value_at(x) == self.UNEXPLORED, self.adjacent_locations()))
        # print("\n\n\n")
        # print("[RETURN TO %s]" %[return_to])
        # print ("AT %s -> " %[self.location], list_of_unexplored_points)
        # self.print_ship()
        return_bot_to = self.location

        for unexplored_point in list_of_unexplored_points:
            # print("Moving to %s" %[unexplored_point], end="==>")
            self.move_robot(self.location_to_direction(unexplored_point))
            self.brain.execute()
            result = self.brain.outputBuffer.pop(0)
            # print (result)
            if result == self.MOVE_SUCCESS:
                self.location = unexplored_point
                self.ship[unexplored_point[1]][unexplored_point[0]] = self.EMPTY
                self.find_oxygen_tank(return_bot_to)
            elif result == self.HIT_WALL:
                self.ship[unexplored_point[1]][unexplored_point[0]] = self.WALL
            elif result == self.OXYGEN_TANK_FOUND:
                self.location = unexplored_point
                self.ship[unexplored_point[1]][unexplored_point[0]] = self.OXYGEN_TANK
                self.find_oxygen_tank(return_bot_to)
                self.oxygen_location = unexplored_point
                # print(self.location)
        if return_to:
            # print("RETURN to %s" % [return_to], end="==>")
            self.move_robot(self.location_to_direction(return_to))
            self.brain.execute()
            result = self.brain.outputBuffer.pop(0)
            self.location = return_to






