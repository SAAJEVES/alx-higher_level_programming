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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"

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

    def update(self, *args, **kwargs):
        """Update Attributes"""
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.__size = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
