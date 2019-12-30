import numpy as np
import math

with open('input.txt', 'r') as myfile:
  data = myfile.read()

def iterate(input_val: str, itr=1, copies=1):
    start_value = input_val * copies
    calcdict = {}
    for iteration in range(itr):
        # print(iteration)
        total_calc = ""
        for i in range(len(start_value)):
            # print("%s / %s" %(iteration*len(start_value)+i, itr*len(start_value)))
            digit_calc = 0
            repeating_pattern = repeating_value(i+1)
            for j in range(len(start_value)):
                digit_calc += int(start_value[j])*repeating_pattern[j % len(repeating_pattern)]
            total_calc += str(digit_calc)[-1]
        start_value=total_calc
    return start_value

def iterate_v2(input_val: str, itr=1, copies=1):
    start_value = input_val * copies
    offset = int(input_val[:7])
    itr_value = start_value[offset:]
    for iteration in range(itr):
        new_value = ""
        print (iteration)
        total = 0
        for i in reversed(itr_value):
            total += int(i)
            new_value = str(total % 10) + new_value
        itr_value = new_value
    return itr_value




def repeating_value(pos):
    ret = []
    for x in [0, 1, 0, -1]:
        for _ in range(pos):
            ret.append(x)
    return ret[1:] + [ret[0]]




