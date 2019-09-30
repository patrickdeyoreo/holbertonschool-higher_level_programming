#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ Print at most x items from a list
    """
    index = 0

    while index < x:
        try:
            print(my_list[index], end="")
        except IndexError:
            break
        else:
            index += 1

    print()

    return index
