#!/usr/bin/python3
'''python script to list
the available attributes and method
of an object
'''


def lookup(obj):
    '''a function that returns the list of available
    attributes and methods of an object

    Args:
        obj:    python object of any type

    Return:
                list of available attributes and method
                of an object
    '''
    return (dir(obj))
