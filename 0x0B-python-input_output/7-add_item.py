#!/usr/bin/python3
'''
module on python json
'''

if __name__ == '__main__':
    load_from_json_file = __import__('6-load_from_json_file').\
            load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    from sys import argv
    from json import loads, dumps

    filename = 'add_item.json'
    try:
        my_list = load_from_json_file(filename)
        for i in range(len(argv)):
            if i > 0:
                my_list.append(argv[i])
        save_to_json_file(my_list, filename)
    except FileNotFoundError:
        my_list = []
        for i in range(len(argv)):
            if i > 0:
                my_list.append(argv[i])
        json_str = dumps(my_list)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)
