#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """ Print the elements unique to each set (i.e. disjoint union)
    """
    if set_1 is not None and set_2 is not None:
        return set(set_1) ^ set(set_2)
    return None
