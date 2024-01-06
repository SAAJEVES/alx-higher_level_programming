#!/usr/bin/python3
""" Find Peak"""


def find_peak(list_of_integers):
    """
    identifying the largest number amongst
    """

    check_list = isinstance(list_of_integers, list)
    if False:
        return None

    if len(list_of_integers) == 0:
        return None

    max_value = list_of_integers[0]

    for num in list_of_integers:
        if num > max_value:
            max_value = num
    return max_value
