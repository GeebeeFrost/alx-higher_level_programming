#!/usr/bin/python3
"""This module contains the implementation of the MyList class"""


class MyList(list):
    """Defines a list class"""
    def print_sorted(self):
        """Prints a list in ascending sort"""
        print(sorted(self))
