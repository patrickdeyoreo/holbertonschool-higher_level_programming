#!/usr/bin/python3
"""Provides a function to serialize the writable attributes of an object"""


def class_to_json(obj):
    """Serialize the writable attributes of an object"""
    return obj.__dict__
