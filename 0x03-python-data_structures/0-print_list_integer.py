#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if my_list is not None:
        list(map(lambda n: print('{}'.format(n)), my_list))
