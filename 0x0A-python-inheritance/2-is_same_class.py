#!/usr/bin/python3
"""This module contains the implementation of is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class
    Args:
        obj: object to be checked
        a_class: class to be checked for
    Returns:
        bool: True if it is an instance, False if not
    """
    return (type(obj) == a_class)
