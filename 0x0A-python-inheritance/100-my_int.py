#!/usr/bin/python3
'''module that manipulates arithmetic operators'''


class MyInt(int):
    '''a class MyInt that inherits from int'''

    def __init(self, real):
        '''MyInt class constructor'''
        self.real = real
    def __eq__(self, other):
        '''changes the normal (==) operator'''
        return (self.real != other.real)

    def __ne__(self, other):
        '''changes the normal (!=) operator'''
        return (self.real == other.real)
