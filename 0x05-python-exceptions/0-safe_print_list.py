#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ Print at most x items from a list
    """
    try:
        for index in range(x):
            print(my_list[index], end="")
    except IndexError:
        return index
    else:
        return index + 1
    finally:
        print()
