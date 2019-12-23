from unittest import TestCase
from intcode import IntcodeComputer

class TestIntcodeComputer(TestCase):
    def test_execute(self):
        self.assertEqual([2, 0, 0, 0, 99], IntcodeComputer([1, 0, 0, 0, 99]).execute().getProgram())
        self.assertEqual([2, 3, 0, 6, 99], IntcodeComputer([2, 3, 0, 3, 99]).execute().getProgram())
        self.assertEqual([2, 4, 4, 5, 99, 9801], IntcodeComputer([2, 4, 4, 5, 99, 0]).execute().getProgram())
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], IntcodeComputer([1, 1, 1, 4, 99, 5, 6, 0, 99]).execute().getProgram())
        self.assertEqual([111, 10, 0, 0, 99], IntcodeComputer([101, 10, 0, 0, 99]).execute().getProgram())
        self.assertEqual([20, 10, 10, 0, 99], IntcodeComputer([1101, 10, 10, 0, 99]).execute().getProgram())
        self.assertEqual([1011, 0, 10, 0, 99], IntcodeComputer([1001, 0, 10, 0, 99]).execute().getProgram())
        self.assertEqual([1002, 4, 3, 4, 99], IntcodeComputer([1002, 4, 3, 4, 33]).execute().getProgram())
        self.assertEqual([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], IntcodeComputer([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]).execute().outputBuffer)
        self.assertEqual(16, len(str(IntcodeComputer([1102, 34915192, 34915192, 7, 4, 7, 99, 0]).execute().outputBuffer[0])))
        self.assertEqual(1125899906842624, IntcodeComputer([ 104, 1125899906842624, 99]).execute().outputBuffer[0])


