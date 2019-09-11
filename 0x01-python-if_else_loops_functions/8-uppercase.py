#!/usr/bin/python3


def uppercase(str):
    """ Prints a string in uppercase (followed by a newline) """
    while str:
        if ord('a') <= ord(str[0]) <= ord('z'):
            print('{:c}'.format(ord(str[0]) & ~0x20), end="")
        else:
            print(str[0], end="")
        str = str[1:]
    print()
