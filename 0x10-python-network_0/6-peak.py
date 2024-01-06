#!/usr/bin/python3
""" Find Peak"""

'''
def find_peak(list_of_integers):
    """
    identifying the largest number amongst
    """

    if not isinstance(list_of_integers, list):
        return None

    if not list_of_integers:
        return None

    max_value = list_of_integers[0]

    for num in list_of_integers:
        if num > max_value:
            max_value = num
    return max_value
'''


def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
