#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """ Create a new list with all occurrences of an element replaced
    """
    if my_list is not None:
        return [x if x != search else replace for x in my_list]
    return None
