#!/usr/bin/python3
"""This module contains the implemenatation of the lookup method"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object
    Args:
        obj (any object): object whose attributes and methods will be returned
    """
    return dir(obj)
