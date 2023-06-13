#!/usr/bin/python3
"""This module contains the class_to_json function"""


def class_to_json(obj):
    """Returns a dictionary description for JSON serialization of an object
    Args:
        obj: instance of a class whose description will be returned
    """
    return (obj.__dict__)
