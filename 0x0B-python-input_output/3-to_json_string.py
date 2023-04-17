#!/usr/bin/python3
'''
returns a JSON representation of
an object string
'''


def to_json_string(my_obj):
    '''
    conver objects to json string

    Args:
        my_obj (str): python object
    Return:
        json string rep
    '''
    import json
    return (json.dumps(my_obj))
