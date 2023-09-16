#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """multiply values by 2"""
    for val in a_dictionary.keys():
        a_dictionary[val] = a_dictionary[val] * 2
    return a_dictionary
