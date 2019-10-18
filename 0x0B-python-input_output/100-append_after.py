#!/usr/bin/python3
"""Provides a function to insert text in a file after specific lines"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text in a file after lines containing a specific string"""
    with open(filename, 'r+') as iostream:
        lines = [
            line + new_string * (search_string in line)
            for line in iostream.readlines()
        ]
        iostream.seek(0)
        iostream.writelines(lines)
