#!/usr/bin/python3
'''
python module on JSON
string
'''


def save_to_json_file(my_obj, filename):
    '''
     writes an Object to a text file
     using a JSON representation.

     Args:
        my_obj (object): python object tp be stored
        filename (text): name of the json text file

    Return:
        the amount of characters written
    '''
    import json
    json_string = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        str_num = f.write(json_string)
    return (str_num)
