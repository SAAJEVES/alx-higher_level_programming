#!/usr/bin/python3
def weight_average(my_list=[]):
    """weighted average"""
    if len(my_list) == 0:
        return 0
    total = 0
    weight = 0

    for tup in my_list:
        total += tup[0] * tup[1]
        weight += tup[1]
    return total/weight
