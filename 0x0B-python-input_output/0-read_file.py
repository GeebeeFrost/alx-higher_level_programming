#!/usr/bin/python3
"""This module contains the implementation of the read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to standard output"""
    with open(filename, mode="rt", encoding="utf-8") as f:
        print(f.read())
