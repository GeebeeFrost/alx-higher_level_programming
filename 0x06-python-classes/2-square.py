#!/usr/bin/python3
"""Implementation of Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Constructor method for Square class

        Args:
            size(int, optional): size of the Square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
