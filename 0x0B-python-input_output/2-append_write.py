#!/usr/bin/python3
'''pythons script on importing'''


def append_write(filename="", text=""):
    '''write_file appent text to a file
    Args:
        filename: naem of the file
        text: string to be written in file
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        chars = f.write(text)
    return(chars)
