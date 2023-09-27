#!/usr/bin/python3

"""Define a class and also initializes it"""
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

    def area(self):
        """The area function
        returns the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Retrive the size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square to a particular value"""
        self.__size = value

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Prints # to the stdout acccording to the 
        value of size
        """
        if self.__size == 0:
            print()
        else:
            for num in range(self.__size):
                print("#" * self.size)
