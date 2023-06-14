#!/usr/bin/python3
'''module on import'''


def append_after(filename="", search_string="", new_string=""):
    '''append a newline after a string
    Args:
        filename (str): name of the file
        search_string (str): string to be encountered before appending
        new_string (str): string to be appended
    '''

    with open(filename, 'r', encoding='utf-8') as f:
        str_list = f.readlines()

    i = 0
    for line in str_list:
        if (line.find(search_string)) != -1:
            str_list.insert(i + 1, new_string)
        i += 1
    text = ''.join(str_list)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
