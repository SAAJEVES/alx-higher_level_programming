#!/usr/bin/python3

"""Creating A Square Class That Inherits From Rectangle"""

Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization Method"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """String Magic Method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {super().width}"

    @property
    def size(self):
        """Size Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
        self.width = self.__size
        self.height = self.__size
