#!/usr/bin/python3
'''Python module that checks for instances
of objects
'''


def is_kind_of_class(obj, a_class):
    '''compere for instances and objects

    Args:
        obj (object):       instance of a class
        a_class (class):    class of object

    Return:
         returns True if the object is an instance of, or if the object is an
         instance of a class that inherited from, the specified class
         otherwise False
    '''
    return (isinstance(obj, a_class))
