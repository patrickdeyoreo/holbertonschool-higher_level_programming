#!/usr/bin/env python3


class Task():
    """ Manage solutions and main functions project tasks
    """

    def __init__(self, func=None, main=None):
        """ Save copies of supplied functions (if any)
        """
        self.func = func
        self.main = main

    def __call__(self):
        """ Execute the main function defined for a task
        """
        return self.main()

    def __repr__(self):
        """ Get info in a form that may be reused as input
        """
        return "{path}(func={func}, main={main})".format(
            func=(None if self.func is None else self.func.__name__),
            main=(None if self.main is None else self.main.__name__),
            path=".".join([self.__module__, self.__class__.__name__])
        )

    def __setattr__(self, name, value):
        """ Assign a function (or None) to a task
        """
        if value is None:
            self.__dict__[name] = value
        elif callable(value):
            self.__dict__[name] = __import__("copy").deepcopy(value)
        else:
            raise TypeError("'{}' object is not callable'".format(
                type(value)
            ))
