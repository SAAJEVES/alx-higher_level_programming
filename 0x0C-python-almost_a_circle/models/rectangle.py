#!/usr/bin/python3

"""Creating the class Rectangle that inherits from Base"""

Base = __import__("base").Base


class Rectangle(Base):
    """A class Called Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization Method"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """Retrieve width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assign new value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """Retrieve x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Assign new value to x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Assign new value to y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
