#!/usr/bin/python3

"""This module contains a Sqaure class"""

class Square:
    """A Square class

    Attributes:
        __size: private field for the size
    """

    def __init__(self, size=0):
        """The initialization function

        Args:
            size(int): size of the square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
