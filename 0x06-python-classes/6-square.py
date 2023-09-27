#!/usr/bin/python3

"""This is about Square Class"""

class Square:
    """A class named Square"""

    def __init__(self, size=0, position=(0,0)):
        """The initialization function"""
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) != int:
            raise TypeError("size must be an integer")
        else:
            self.__size == size


        if type(position) != tuple or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int or len(position) != 2:
            raise TypeError("position must be a tuple of 2  positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Retriving size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieving Position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting Position"""
        if type(value) != tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int or len(value) != 2:
            raise TypeError("position must be a tuple of 2  positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square shape using the # sign"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
