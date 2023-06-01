#!/usr/bin/python3
"""Implementation of Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Constrcut a new square
        Args:
            size(int, optional): size of the Square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of a Square object
        Returns:
            The area of a Square object
        """
        return (self.__size ** 2)
