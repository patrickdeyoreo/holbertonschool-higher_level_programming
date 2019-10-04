#!/usr/bin/python3
"""Provides a function 'add' that adds two numbers"""


def add(a, b=98):
    """Add two integers"""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
