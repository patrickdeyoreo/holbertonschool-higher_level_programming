#!/usr/bin/python3


def common_elements(set_1, set_2):
    """ Print the elements common to two sets (i.e. union)
    """
    if set_1 is not None and set_2 is not None:
        return set(set_1) & set(set_2)
    return None
