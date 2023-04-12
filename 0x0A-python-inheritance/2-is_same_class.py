#!/usr/bin/python3
'''Python module that checks for instances
of objects
'''


def is_same_class(obj, a_class):
    '''compere for instances and objects

    Args:
        obj (object):       instance of a class
        a_class (class):    class of object

    Return:
             returns True if the object is exactly an instance
             of the specified class ; otherwise False
    '''
    return (True if (type(obj) == a_class) else False)
