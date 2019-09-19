#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """ Create a new dictionary with all values doubled
    """
    if a_dictionary is not None:
        return {key: 2 * val for key, val in a_dictionary.items()}
    return None
