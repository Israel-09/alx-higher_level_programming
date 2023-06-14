#!/usr/bin/python3
'''python script on import'''


def to_json_string(my_obj):
    import json
    '''convert a python object to a 
    json string

    Args:
        my_obj (obj): object to be converted
    '''
    return (json.dumps(my_obj))

