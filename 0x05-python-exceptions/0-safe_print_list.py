#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ Print at most x items from a list
    """
    for index in range(x):
        try:
            print(my_list[index], end="")
        except IndexError:
            break

    if index:
        print()

    return index
