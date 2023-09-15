#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints the sorted diction"""
    ordered = sorted(a_dictionary)

    for val in ordered:
        print("{}: {}".format(val, a_dictionary[val]))
