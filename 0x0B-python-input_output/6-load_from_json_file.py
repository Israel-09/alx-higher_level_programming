#!/usr/bin/python3
'''
module on pythom json
'''


def load_from_json_file(filename):
    '''creates an Object from a “JSON file”

    Args:
        filename: name of the file that contains
        the string
    '''
    import json
    with open(filename, encoding='utf-8') as f:
        j_string = f.readline()
    return (json.loads(j_string))
