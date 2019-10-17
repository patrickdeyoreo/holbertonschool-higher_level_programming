#!/usr/bin/python3
""" Provides a class to represent squares
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Definition of fixed-size square
    """
    def __init__(self, size):
        """ Instantiate a square
        """
        try:
            super().__init__(size, size)
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = size
