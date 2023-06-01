#!/usr/bin/python3
"""Implementation of Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Constructs a new square
        Args:
            size(int, optional): size of the Square object
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of a square object"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of a Square object
        Returns:
            The area of a Square object
        """
        return (self.__size ** 2)
