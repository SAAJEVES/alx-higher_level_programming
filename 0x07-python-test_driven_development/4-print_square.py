#!/usr/bin/python3
"""Function that prints a square with the character #.
"""


def print_square(size):
    """prints a square with the character #

    Args:
        size (int): size length of the square
    """
    err1 = "size must be an integer"

    if type(size) == float and size < 0:
        raise TypeError(err1)

    if type(size) != int:
        raise TypeError(err1)

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
