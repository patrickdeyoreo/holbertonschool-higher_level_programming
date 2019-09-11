#!/usr/bin/python3


def print_last_digit(number):
    """
    Prints and returns the last digit of a number.
    If given something that's not a number, this returns None.
    """
    if not isinstance(number, int):
        return (None)
    number = str(number)[-1]
    print(number, end="")
    return (int(number))
