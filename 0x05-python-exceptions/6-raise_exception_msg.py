#!/usr/bin/python3
def raise_exception_msg(message=""):
    """function that raises a name exception with a message

    Args:
        message (string): the string message

    Return:
        raises an exception and print to standard error a customized message
    """
    raise NameError(message)
