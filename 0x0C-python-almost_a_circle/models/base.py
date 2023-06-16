#!/usr/bin/python3
"""This module contains the base class"""


class Base:
    """Base class of project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
