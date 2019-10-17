#!/usr/bin/python3
"""Provides a function to write a JSON repr. of an object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a file"""
    with open(filename, 'w') as ostream:
        return json.dump(my_obj, ostream)
