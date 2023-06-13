#!/usr/bin/python
"""This module contains the implementation of the read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to standard output"""
    if filename:
        with open(filename, mode='r', encoding="utf-8") as f:
            print(f.read())
