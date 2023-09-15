#!/usr/bin/python3
def uniq_add(my_list=[]):
    """This add up elements in a list without adding an element twice"""
    total = 0
    unique = []
    for val in my_list:
        if val not in unique:
            unique.append(val)
            total += val
    return total
