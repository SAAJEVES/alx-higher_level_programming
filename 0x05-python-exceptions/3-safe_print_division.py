#!/usr/bin/python3
def safe_print_division(a, b):
    """function that divides 2 integers and prints the result.

    Args:
        a (int): divisor
        b (int): quotient

    Returns:
        Without error a float
        When an error occurs, None
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
