#!/usr/bin/python3
def safe_print_integer(value):
    """Safe print integer

    Args:
        value (any type): could be of any type

    Returns:
        An integer if value is an integer
    """

    try:
        print("{:d}".format(value))
        return True
    except:
        return False
