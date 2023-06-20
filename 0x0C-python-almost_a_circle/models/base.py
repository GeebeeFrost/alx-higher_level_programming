#!/usr/bin/python3
"""This module contains the base class"""
import json


class Base:
    """Base class of project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list of objects to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) < 1:
                f.write("[]")
            else:
                ls_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(ls_dict))
