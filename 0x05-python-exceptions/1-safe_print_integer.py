#!/usr/bin/python3
def safe_print_integer(value):
    """Safe print integer

    Args:
        value (int): could be of any type

    Returns:
        An integer if value is an integer
    """
    try:
        print("{:d}".format(value))
        return True
    except BaseException:
        return False
