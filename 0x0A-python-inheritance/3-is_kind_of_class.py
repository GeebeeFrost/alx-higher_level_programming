#!/usr/bin/python3
"""This module contains the implementation of is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a specified class
    or a class inherited from that class
    Args:
        obj: object to be checked
        a_class: class to be checked for
    Returns:
        bool: True if it is an instance, False if not
    """
    return (isinstance(obj, a_class))
