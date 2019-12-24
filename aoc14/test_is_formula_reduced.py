from unittest import TestCase
from aoc14 import is_formula_reduced, index_of_reduceable, add_to_formula, min_runs

class TestIs_formula_reduced(TestCase):
    def test_is_formula_reduced(self):
        self.assertFalse(is_formula_reduced([["FUEL",1]]))
        self.assertFalse(is_formula_reduced([["XXDF", 1],["FSDF", 3], ["ORE", 4343], ["GGDS", -3]]))
        self.assertTrue(is_formula_reduced([["ORE", 4343], ["GGDS", -3]]))

    def test_index_of_reduceable(self):
        self.assertEqual(0, index_of_reduceable([["FUEL", 1]]))
        self.assertEqual(0, index_of_reduceable([["XXDF", 1], ["FSDF", 3], ["ORE", 4343], ["GGDS", -3]]))
        self.assertEqual(1, index_of_reduceable([["ORE", 4343], ["FSDS", 4], ["GGDS", -3]]))
        self.assertEqual(2, index_of_reduceable([["ORE", 4343], ["GGDS", -3], ["FSDS", 4]]))

    def test_add_to_formula(self):
        formula = [["FUEL", 1]]
        add_to_formula(formula, "BC", 1)
        self.assertEqual([["FUEL", 1], ["BC", 1]], formula)

        formula = [["ORE", 156], ["BC", 5]]
        add_to_formula(formula, "BC", 1)
        self.assertEqual([["ORE", 156], ["BC", 6]], formula)

        formula = [["ORE", 156], ["BC", -5]]
        add_to_formula(formula, "BC", 1)
        self.assertEqual([["ORE", 156], ["BC", -4]], formula)

        formula = [["ORE", 156], ["BC", -5]]
        add_to_formula(formula, "ORE", 100)
        add_to_formula(formula, "CD", 4)
        add_to_formula(formula, "ORE", -40)
        add_to_formula(formula, "BC", 4)
        self.assertEqual([["ORE", 216], ["BC", -1], ["CD", 4]], formula)

    def test_min_runs(self):
        self.assertEqual(10, min_runs)