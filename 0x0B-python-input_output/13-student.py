#!/usr/bin/python3
"""Provides a class to represent a student"""


class Student:
    """Definition of a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiate a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a JSON representation of a student"""
        if isinstance(attrs, list) and all(
                map(lambda s: isinstance(s, str), attrs)
        ):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Load data from a JSON representation of a student"""
        self.__dict__.update(json)
