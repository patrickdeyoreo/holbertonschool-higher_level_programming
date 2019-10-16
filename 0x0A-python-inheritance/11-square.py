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
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Render a string representation of a square
        """
        return '[Square] {size}/{size}'.format(size=self.__size)

    def area(self):
        """ Calculate the area of a square
        """
        return super().area()
