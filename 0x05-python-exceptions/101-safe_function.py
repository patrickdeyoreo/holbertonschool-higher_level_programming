#!/usr/bin/python3
def safe_function(fct, *args):
    """ Execute a function
    """
    try:
        return fct(*args)
    except Exception as e:
        print('Exception: {}\n'.format(e), file=__import__('sys').stderr)
        return None
