from reactions import *
import math
from numpy import loadtxt
import numpy as np
from utils import import_text_file

reactions = reaction_list_to_dict(list(map(lambda x: Reaction(x), import_text_file("input.txt"))))

def find_formula_for(reaction: str):
    return reactions[reaction]

current_formula = [["FUEL", 3126714]]

def index_of_reduceable(formula):
    return list(map(lambda x: x[0] != "ORE" and x[1] > 0, formula)).index(True)

def is_formula_reduced(formula):
    return all(map(lambda x: x[0] == "ORE" or x[1] <= 0, formula))

def add_to_formula(formula, element, qty):
    for item in formula:
        if item[0] == element:
            item[1] += qty
            return
    formula.append([element, qty])

def print_formula(formula):
    for item in formula:
        print ("[%s] %s +" %(item[1], item[0]), end='')
    print("\n")

def print_elem(formula,elem):
    for item in formula:
        if (item[0] == elem):
            print(item)

while not is_formula_reduced(current_formula):
    print_formula(current_formula)
    item_to_reduce = current_formula.pop(index_of_reduceable(current_formula))
    reaction = reactions[item_to_reduce[0]]
    min_runs = math.ceil(item_to_reduce[1]/reaction.yield_qty)
    leftovers = min_runs*reaction.yield_qty - item_to_reduce[1]
    for reagent,qty in reaction.reagents.items():
        add_to_formula(current_formula, reagent, qty*min_runs)
    add_to_formula(current_formula, item_to_reduce[0], -leftovers)

print_formula(current_formula)
print_elem(current_formula, "ORE")



