#!/usr/bin/python3
"""Integer addition

"""


def add_integer(a, b=98):
    """Adds 2 integers

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        the addition i.e a + b;
        error if a (or b) is not an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
