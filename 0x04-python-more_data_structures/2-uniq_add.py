#!/usr/bin/python3


def uniq_add(my_list=[]):
    """ Sum all unique integers in a list
    """
    if my_list is not None:
        return sum(set(my_list))
    return None
