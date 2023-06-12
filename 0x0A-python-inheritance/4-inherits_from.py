#!/usr/bin/python3
"""This module contains the implementation of the inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a subclass of a class
    Args:
        obj: object to be checked
        a_class: class to be checked for
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
