#!/usr/bin/python3
"""Provides a class to represent a student"""


class Student:
    """Definition of a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiate a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a JSON representation of a student"""
        return self.__dict__
