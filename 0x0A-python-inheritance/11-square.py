#!/usr/bin/python3
"""This module contains the implementation of the Square class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
