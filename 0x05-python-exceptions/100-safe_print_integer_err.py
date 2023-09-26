#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """function that prints an integer

    Args:
        value (int): an integer

    Returns:
        If true prints an integer
        If false, write to the stderr
    """
    try:
        print("{:d}".format(value))
        return True
    except BaseException as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
