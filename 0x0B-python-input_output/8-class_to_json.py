#!/usr/bin/python3
'''
module on json strings
'''


def class_to_json(obj):
    '''returns the dictionary description with simple data structure
    for JSON serialization of an object:

        Args:
            obj (object): an instance of a class

        Returns:
            Dictionary discription of an object
    '''
    my_dict = obj.__dict__
    return (my_dict)
