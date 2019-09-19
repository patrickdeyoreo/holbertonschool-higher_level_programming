#!/usr/bin/python3


def best_score(a_dictionary):
    """ Retrieve the a key of the largest integer value
    """
    if a_dictionary:
        return max(a_dictionary.items(),
                   key=lambda pair: pair[1],
                   default=None)
    return None
