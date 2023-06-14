#!/usr/bin/python3
'''pythons script on importing'''


def write_file(filename="", text=""):
    '''write_file write to a file
    Args:
        filename: naem of the file
        text: string to be written in file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        chars = f.write(text)
    return(chars);
