#!/usr/bin/python3


def uppercase(s):
    """ Prints a string in uppercase (followed by a newline) """
    while s:
        if ord('a') <= ord(s[0]) <= ord('z'):
            print('{:c}'.format(ord(s[0]) & ~0x20), end="")
        else:
            print(s[0], end="")
        s = s[1:]
    print()
