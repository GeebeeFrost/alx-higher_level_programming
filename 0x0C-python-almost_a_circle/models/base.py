#!/usr/bin/python3
"""This module contains the base class"""
import json
import os
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dicts represented by a JSON string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

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

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of the calling class from a file"""
        filename = "{}.json".format(cls.__name__)
        ls_instances = []
        ls_dicts = []
        if os.path.exists(filename):
            with open(filename, mode='r') as f:
                js = f.read()
                ls_dicts = cls.from_json_string(js)
                for dct in ls_dicts:
                    ls_instances.append(cls.create(**dct))
        return ls_instances

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dum = cls(2, 1)
        elif cls.__name__ == "Square":
            dum = cls(4)
        dum.update(**dictionary)
        return dum

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV representation of list of objects to a file"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) < 1:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """"Returns a list of instances of the calling class from a file"""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode="r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fields)
                list_dicts = [dict([k, int(v)]
                                   for k, v in d.items()) for d in reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
