#!/usr/bin/python3
'''
module contains a class locked attribute
'''


class LockedClass:
    '''class with a locked attribute first_name'''

    @property
    def first_name(self):
        pass

    @first_name.setter
    def first_name(self, value):
        message = "'LockedClass' object has no attribute 'first_name'"
        raise AttributeError(message)
