#!/usr/bin/python3
"""This module contains the implementation of the append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args:
        filename: file to append string to
        text: string to be appended
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
