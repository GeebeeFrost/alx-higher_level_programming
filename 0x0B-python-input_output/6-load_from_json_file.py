#!/usr/bin/python3
"""This module contains the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args:
        filename: file to get object from
    """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
