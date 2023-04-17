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
