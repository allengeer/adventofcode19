from unittest import TestCase
from aoc5 import executeIntcode

class TestExecuteIntcode(TestCase):
    def test_executeIntcode(self):
        self.assertEquals([2,0,0,0,99], executeIntcode([1,0,0,0,99]))
        self.assertEquals([2,3,0,6,99], executeIntcode([2,3,0,3,99]))
        self.assertEquals([2,4,4,5,99,9801], executeIntcode([2,4,4,5,99,0]))
        self.assertEquals([30,1,1,4,2,5,6,0,99], executeIntcode([1,1,1,4,99,5,6,0,99]))
        self.assertEquals([111, 10, 0, 0, 99], executeIntcode([101, 10, 0, 0, 99]))
        self.assertEquals([20, 10, 10, 0, 99], executeIntcode([1101, 10, 10, 0, 99]))
        self.assertEquals([1011, 0, 10, 0, 99], executeIntcode([1001, 0, 10, 0, 99]))
        self.assertEquals([1002,4,3,4,99], executeIntcode([1002,4,3,4,33]))
