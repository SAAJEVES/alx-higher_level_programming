#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """multiply each elements in a list by a particular value"""
    return list(map(lambda x: x * number, my_list))
