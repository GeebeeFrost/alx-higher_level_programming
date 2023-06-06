#!/usr/bin/python3
"""This module contains the implementation of the add_integer function"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: first integer
        b: second integer

    Returns:
        Sum of the two integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
