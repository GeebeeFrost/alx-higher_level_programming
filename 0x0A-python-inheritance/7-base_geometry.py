#!/usr/bin/python3
"""This module contains the implementation of the BaseGeometry class"""


class BaseGeometry:
    """Defines a BaseGeometry"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
            name (str): name of value
            value (int): value of name
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
