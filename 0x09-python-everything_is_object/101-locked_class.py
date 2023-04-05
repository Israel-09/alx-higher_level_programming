#!/usr/bin/python3
'''
module contains a class locked attribute
'''


class LockedClass:
    '''class with a locked attribute first_name'''

    @property
    def last_name(self):
        pass

    @last_name.setter
    def last_name(self, value):
        message = "'LockedClass' object has no attribute 'last_name'"
        raise AttributeError(message)
