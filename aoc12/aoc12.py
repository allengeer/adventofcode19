from numpy import loadtxt
import numpy as np
from intcode import IntcodeComputer
import itertools

input_program = list(loadtxt("input.txt", dtype=str))
X=0
Y=1
Z=2
class Moon:
    def __init__(self, location_text):
        self.location = (int(location_text[0].split("=")[1][:-1]), int(location_text[1].split("=")[1][:-1]), int(location_text[2].split("=")[1][:-1]))
        self.velocity = (0,0,0)

    def apply_gravity(self, other_body):
        dx = 0 if not (self.location[X] - other_body.location[X]) else (self.location[X] - other_body.location[X]) / abs(self.location[X] - other_body.location[X])
        dy = 0 if not (self.location[Y] - other_body.location[Y]) else (self.location[Y] - other_body.location[Y]) / abs(self.location[Y] - other_body.location[Y])
        dz = 0 if not (self.location[Z] - other_body.location[Z]) else (self.location[Z] - other_body.location[Z]) / abs(self.location[Z] - other_body.location[Z])
        self.velocity = tuple(map(lambda x, y: x + y, self.velocity,  (-dx,-dy,-dz)))
        other_body.velocity = tuple(map(lambda x, y: x + y, other_body.velocity, (dx, dy, dz)))

    def apply_velocity(self):
        self.location = tuple(map(lambda x, y: x + y, self.velocity, self.location))

    def kin_energy(self):
        return abs(self.velocity[X]) + abs(self.velocity[Y]) + abs(self.velocity[Z])

    def pot_energy(self):
        return abs(self.location[X]) + abs(self.location[Y]) + abs(self.location[Z])

    def tot_energy(self):
        return self.kin_energy() * self.pot_energy()

moons = []
for _ in input_program:
    moons.append(Moon(_))

def print_moons(moons):
    for moon in moons:
        print("\t%s -> %s" %(moon.location, moon.velocity,))

def total_energy(moons):
    return sum(map(lambda x: x.tot_energy(), moons))



n = 10000
i = 0;
start_xstate = ()
start_ystate = ()
start_zstate = ()

for moon in moons:
    start_xstate += (moon.location[X], moon.velocity[X])
    start_ystate += (moon.location[Y], moon.velocity[Y])
    start_zstate += (moon.location[Z], moon.velocity[Z])
p_x = None
p_y = None
p_z = None
pairs = list(itertools.combinations(range(len(moons)), 2))
while not p_x or not p_y or not p_z:
    print("Iteration %s -> Energy %s" %(i, total_energy(moons)))
    # print_moons(moons)

    xstate = ()
    ystate = ()
    zstate = ()
    for pair in pairs:
        moons[pair[0]].apply_gravity(moons[pair[1]])
    for moon in moons:
        moon.apply_velocity()
        xstate += (moon.location[X], moon.velocity[X])
        ystate += (moon.location[Y], moon.velocity[Y])
        zstate += (moon.location[Z], moon.velocity[Z])
    if start_xstate == xstate and not p_x:
        p_x = i
    if start_ystate == ystate and not p_y:
        p_y = i
    if start_zstate == zstate and not p_z:
        p_z = i
    i += 1
print (np.lcm.reduce([p_x+1,p_y+1,p_z+1]))
