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
        try:
            if size < 0:
                raise ValueError
            elif type(size) != int:
                raise TypeError
            else:
                self.__size = size
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
