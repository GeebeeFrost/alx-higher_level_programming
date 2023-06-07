#!/usr/bin/python3
"""This module contains the implementation for the say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints an introduction
    Args:
        first_name (string): first name
        last_name (string, optional): last name
    """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
