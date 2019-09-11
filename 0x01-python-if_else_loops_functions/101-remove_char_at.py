#!/usr/bin/python3


def remove_char_at(str, n):
    """ Copy a string and remove a character at n """
    return str[:n] + str[(len(str) + n) % len(str) + 1:]
