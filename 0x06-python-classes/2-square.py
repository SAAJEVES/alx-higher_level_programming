#!/usr/bin/python3

"""This module contains a Sqaure class"""

class Square:
    """A Square class
    """

    def __init__(self, size=0):
        """The initialization function
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
