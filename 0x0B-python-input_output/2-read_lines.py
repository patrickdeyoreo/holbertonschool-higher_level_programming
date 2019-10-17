#!/usr/bin/python3
"""Provides a function to print a poriton of a file"""


def read_lines(filename="", nb_lines=0):
    """Print the specified number of lines of a file"""
    with open(filename, 'r') as istream:
        if nb_lines < 1:
            print(istream.read(), end="")
        else:
            while nb_lines > 0:
                line = istream.readline()
                if line:
                    print(line, end="")
                    nb_lines -= 1
                else:
                    break
