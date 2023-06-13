#!/usr/bin/python3
"""This module contains the implementation of the from_json_string function"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string
    Args:
        my_str: JSON string to decode
    """
    return (json.loads(my_str))
