from unittest import TestCase
from aoc1 import *

class TestFuelRequired(TestCase):
    def test_fuelRequired(self):
        self.assertEqual(2, fuelRequired(12))
        self.assertEqual(2, fuelRequired(14))
        self.assertEqual(654, fuelRequired(1969))
        self.assertEqual(33583, fuelRequired(100756))
        self.assertEqual(45950, fuelRequired(137857))

    def test_totalFuelRequired(self):
        self.assertEqual(2, totalFuelRequired(14))
        self.assertEqual(966, totalFuelRequired(1969))
        self.assertEqual(50346, totalFuelRequired(100756))