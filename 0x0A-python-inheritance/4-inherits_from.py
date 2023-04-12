#!/usr/bin/python3
'''module on python inheritance'''


def inherits_from(obj, a_class):
    '''
    checks if an object is inherited from a class

    Args:
        obj (object):       object to be checked
        a_class (class):    class to compare with

    Return:
            returns True if the object is an instance of a class that 
            inherited (directly or indirectly) from the specified class
            otherwise False.
    '''
    return (issubclass(obj, a_class))
