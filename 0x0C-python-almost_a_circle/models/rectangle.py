#!/usr/bin/python3

"""Creating the class Rectangle that inherits from Base"""

Base = __import__("base").Base


class Rectangle(Base):
    """A class Called Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization Method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        """Retrieve height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assign new value to height"""
        self.__height = value

    @property
    def width(self):
        """Retrieve width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assign new value to width"""
        self.__width = value

    @property
    def x(self):
        """Retrieve x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Assign new value to x"""
        self.__x = value

    @property
    def y(self):
        """Retrieve y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Assign new value to y"""
        self.__y = value
