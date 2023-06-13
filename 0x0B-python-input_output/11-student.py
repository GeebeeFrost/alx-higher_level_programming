#!/usr/bin/python3
"""This module contains the Student class"""


class Student():
    """Defines a student
    Attributes:
        first_name: student's first name
        last_name: student's last name
        age: student's age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of attributes of a student
        Args:
            attrs (list of strings): attrs to retrieve
        """
        if (type(attrs) == list and all(type(attr) == str for attr in attrs)):
            return ({attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)})
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of a student
        Args:
            json: dictionary containing new attributes
        """
        for k, v in json.items():
            setattr(self, k, v)
