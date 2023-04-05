#!/usr/bin/python3
'''
module contains a class locked attribute
'''


class LockedClass:
    '''class with a locked attribute first_name'''
    @property
    def last_name(self):
        raise AttributeError("'LockedClass' object has no attribute 'last_name'")

    @last_name.setter
    def last_name(self, value):
        raise AttributeError("'LockedClass' object has no attribute 'last_name'")
