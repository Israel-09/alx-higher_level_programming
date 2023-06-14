#!/usr/bin/python3
'''python script on import'''
import json


def to_json_string(my_obj):
    '''convert a python object to a
    json string

    Args:
        my_obj (obj): object to be converted

    Return:
        A string representation of the my_obj
    '''
    return (json.dumps(my_obj))
