#!/usr/bin/python3
'''
module contains a class locked attribute
'''


class LockedClass:
    '''class with a locked attribute first_name'''

    __slots__ = ['first_name']

    def __init__(self):
        first_name = None
