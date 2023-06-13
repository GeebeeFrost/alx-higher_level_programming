#!/usr/bin/python3
"""This module contains the implementation of the to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Args:
        my_obj: object to be serialized
    """
    return (json.dumps(my_obj))
