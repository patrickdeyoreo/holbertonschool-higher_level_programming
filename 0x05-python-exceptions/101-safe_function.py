#!/usr/bin/python3
def safe_function(fct, *args):
    """ Execute a function
    """
    try:
        return fct(*args)

    except:
        __import__('sys').stderr.write('Exception: {}\n'.format(
            __import__('sys').exc_info()[1]
        ))
        return None
