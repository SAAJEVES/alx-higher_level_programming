#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """multiply values by 2"""
    new_dict = {}
    for key in a_dictionary.keys():
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
