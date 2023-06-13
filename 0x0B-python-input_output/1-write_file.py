#!/usr/bin/python3
"""This module contains the implementation of the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Args:
        filename: file to write text to
        text: text to write
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
