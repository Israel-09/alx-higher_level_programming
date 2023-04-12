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
