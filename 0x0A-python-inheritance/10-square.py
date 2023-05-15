#!/usr/bin/env python3
"""module on a square class"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    '''square class that inherits from Rectangle'''
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''
        returns the area of a square object
        '''
        return (self.__size ** 2)
