#!/usr/bin/python3
'''
python script on JSON
'''


def from_json_string(my_str):
    '''
    returns an object (Python data structure)
    represented by a JSON string
    
    Args:
        my_str (str): json string to be coverted 
        to an object
    Return:
        returns an object (Python data structure)
        represented by a JSON string
    '''
    import json
    obj = json.loads(my_str)
    return (obj)

