#!/usr/bin/python3


def weight_average(my_list=[]):
    """ Compute the weighted average of values in the tuple (<score>, <weight>)
    """
    if my_list:
        return sum((v * w for v, w in my_list)) / sum((w for _, w in my_list))
    if my_list == []:
        return 0
    return None
