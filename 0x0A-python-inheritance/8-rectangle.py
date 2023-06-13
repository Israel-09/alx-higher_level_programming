#!/usr/bin/python3
'''
module that contains a rectangle class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    rectangle class that inherits atteibute of basegeoometry
    '''
    def __init__(self, width, height):
        '''contructor for Rectangle instances

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
