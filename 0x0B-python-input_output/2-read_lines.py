#!/usr/bin/python3
"""Provides a function to print a poriton of a file"""


def read_lines(filename="", nb_lines=0):
    """Print the specified number of lines of a file"""
    with open(filename, 'r') as istream:
        lines = istream.readlines()
        print(*lines[:nb_lines if nb_lines > 0 else len(lines)],
              sep="\n", end="")
