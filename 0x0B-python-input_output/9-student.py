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

    def to_json(self):
        """Returns dictionary representation of an instance"""
        return self.__dict__
