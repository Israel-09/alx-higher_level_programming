#!/usr/bin/python3
"""
python script to read a file
"""

def read_file(filename=""):
    '''read_file reads a file with name filename
    and prints it to stout

    Args:
        filename (str): name of the file to be read
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.readlines()

    print(''.join(text))
