#!/usr/bin/python3


def _reduce(fn, ls, init=0):
    """ Reduce a list to a single value
    """
    if ls:
        return _reduce(fn, ls[1:], fn(init, ls[0]))
    return init


def roman_to_int(roman_string):
    """ Convert a Roman numeral to an integer
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
        return _reduce(
            lambda l, r: r + l if r <= l else r - l,
            list(map(n2n.get, roman_string.upper())),
        )
    except (KeyError, TypeError):
        return 0
