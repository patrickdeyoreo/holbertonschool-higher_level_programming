#!/usr/bin/python3
"""
Provides a function to find a peak element in an unsorted list of integers
"""


def find_peak(integers):
    """
    Finds a peak element in an unsorted list of integers
    """
    if len(integers) == 0:
        return None
    if len(integers) == 1:
        return integers[0]
    if len(integers) == 2:
        return integers[0] if integers[0] < integers[1] else integers[1]
    if integers[len(integers) // 2] < integers[len(integers) // 2 - 1]:
        return find_peak(integers[:len(integers) // 2])
    if integers[len(integers) // 2] < integers[len(integers) // 2 + 1]:
        return find_peak(integers[len(integers) // 2:])
    return integers[len(integers) // 2]
