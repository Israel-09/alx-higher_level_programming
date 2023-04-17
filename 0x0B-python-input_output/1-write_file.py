#!/usr/bin/python3
'''
module to create if not in existence
and write to an existing file
'''


def write_file(filename="", text=""):
    '''
    writes a string to a text file (UTF8) and returns the
    number of characters written.

    Args:
        filename (str): name of file to be created
        text (str):     text to be written to the file

    Return:
        Returns:        the number of characters written
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        chars_num = f.write(text)
    return (chars_num)

