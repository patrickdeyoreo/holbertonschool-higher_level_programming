#!/usr/bin/python3


def uppercase(s):
    """ Prints a string in uppercase (followed by a newline) """
    print(s.translate({(c | 32): c for c in range(ord('A'), ord('Z') + 1)}))
