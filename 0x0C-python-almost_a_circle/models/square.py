#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Creates a new square instance"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """Returns a string representation of a square instance"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.size))

    @property
    def size(self):
        """Defines the length of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of a square"""
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
