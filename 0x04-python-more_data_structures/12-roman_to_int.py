#!/usr/bin/python3

from functools import reduce


def roman_to_int(roman_string):
    """ Convert Roman numerals to integers
    """
    n2n = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
    }
    try:
        return reduce(
            lambda l, r: r - l if l < r  else r + l,
            map(n2n.get, roman_string.upper())
        )
    except (KeyError, TypeError):
        return 0
