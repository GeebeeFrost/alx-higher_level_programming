#!/usr/bin/python3
"""This module contains the implementation for the print_square function"""


def print_square(size):
    """Prints a square with the character #
    Args:
        size (int): size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("#", end='')
        print()
