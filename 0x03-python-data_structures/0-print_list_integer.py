#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if my_list is not None:
        print('\n'.join(['{}'.format(n) for n in my_list]))
