#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """function that executes a function safely

    Args:
        fct: a function 
        args: a tuple

    Returns:
        returns a result or None
    """
    try:
        value = fct(*args)
        return value
    except BaseException as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
