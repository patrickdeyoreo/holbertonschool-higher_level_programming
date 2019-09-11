#!/usr/bin/python3


def print_last_digit(number):
    """ Prints and returns the last digit of a number """
    number = str(number)[-1]
    print(number, end="")
    return (int(number))
