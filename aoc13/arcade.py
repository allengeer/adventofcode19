import numpy as np
class Arcade:
    def __init__(self, size):
        self.screen = np.zeros(size, dtype=int)
        self.score = 0

    def resize(self, size):
        target = np.zeros(size, dtype=int)
        target[:self.screen.shape[0], :self.screen.shape[1]] = self.screen
        self.screen = target

    def read_location(self, x, y):
        if y >= self.screen.shape[0] or x >= self.screen.shape[1]:
            self.resize((max(y+1, self.screen.shape[0]),max(x+1, self.screen.shape[1])))
        return self.screen[y][x]

    def write_location(self, x, y, val):
        # print("%s,%s,%s" %(x,y,val))
        if y >= self.screen.shape[0] or x >= self.screen.shape[1]:
            self.resize((max(y + 1, self.screen.shape[0]), max(x + 1, self.screen.shape[1])))
        self.screen[y][x] = val