#!/usr/bin/python3
'''
opens a .txt file if it exist otherwise create
a new .txt file and append a test to the file
'''


def append_write(filename="", text=""):
    '''
    appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): name of the file
        text (str):     text to be appended

    Return:
        The number of characters appended
    '''
    with open(filename, 'a',  encoding='utf-8') as f:
        chars_num = f.write(text)
    return (chars_num)
