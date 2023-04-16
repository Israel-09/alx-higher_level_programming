#!/usr/bin/python3
'''
python module on file i/o
'''


def read_file(filename=""):
    ''' reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): name of the textfile
    '''
    with open(filename) as f:
        text = f.read()
    print(text, end='')
