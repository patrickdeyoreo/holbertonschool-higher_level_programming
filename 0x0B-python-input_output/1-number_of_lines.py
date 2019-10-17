#!/usr/bin/python3
"""Provides a function to count the lines in a file"""


def number_of_lines(filename=""):
    """Count the number of lines in a file"""
    with open(filename, 'r') as istream:
        return len(istream.readlines())
