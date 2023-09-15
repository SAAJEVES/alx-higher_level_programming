#!/usr/bin/python3
def number_keys(a_dictionary):
    """This returns the number of keys in a dictionary"""
    dict_keys = a_dictionary.keys()
    list_keys = list(dict_keys)
    len_keys = len(list_keys)
    return len_keys
