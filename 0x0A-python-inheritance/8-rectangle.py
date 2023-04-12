#!/usr/bin/python3
'''
file that containns a empty class
'''


class BaseGeometry:
    '''
    a class that defines a basegeometry
    '''

    def area(self):
        '''
        calculates the area of a geometry

        Raise:
            Excpetion: area() is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value

        Args:
            name (string): name
            value (int): value

        Raise:
            TypeError: if value is not an integer
            ValueError: if valye is less than zero
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
        self.integer_valudator('height', height)
        self.__height = height
