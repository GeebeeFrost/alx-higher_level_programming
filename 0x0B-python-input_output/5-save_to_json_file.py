#!/usr/bin/python3
"""This module contains the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation
    Args:
        my_obj: object to be serialized to JSON format
        filename: file to be written to
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
