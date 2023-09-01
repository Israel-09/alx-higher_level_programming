#!/usr/bin/python3
'''python module on a rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''definition of a rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor for rectangle instances
        Args:
        width (int): the width of the rectangle
        height (int): the width of the rectangle

        Raises:
            ValueError: if the arguement are of invalid value
            TypeError: if the arguements are of invalid types
        '''
        super().__init__(id)
        self.validator('width', width)
        self.__width = width
        self.validator('height', height)
        self.__height = height
        self.validator('x', x)
        self.__x = x
        self.validator('y', y)
        self.__y = y

    @property
    def width(self):
        '''getter method for width field'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        setter method for width private attribute
        Args:
            value (int): value to replace the width
        '''
        self.validator('width', value)
        self.__width = value

    @property
    def height(self):
        '''getter method for height field'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter method for height private attribute
        Args:
            value (int): value to replace the height
        '''
        self.validator('height', value)
        self.__height = value

    @property
    def x(self):
        '''getter method for attribute x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter method for x private attribute
        Args:
            value (int): value to replace the x
        '''
        self.validator('x', value)
        self.__x = value

    @property
    def y(self):
        '''getter method for y field'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter method for y private attribute
        Args:
            value (int): value to replace the y
        '''
        self.validator('y', value)
        self.__y = value

    @staticmethod
    def validator(attr, value):
        '''validates the attributes'''

        if type(value) is not int:
            raise TypeError(f"{attr} must be an integer")
        if attr == 'x' or attr == 'y':
            if value < 0:
                raise ValueError(f"{attr} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{attr} must be > 0")

    def area(self):
        '''returns the area of the rectangle'''
        return (self.__width * self.__height)

    def display(self):
        '''displays the rectangle'''

        '''handles the y-axis'''
        for y_ax in range(self.__y):
            print()

        for i in range(self.__height):
            '''handles the x axis'''
            for x_ax in range(self.__x):
                print(' ', end='')

            for j in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        ''' assigns a new value to attributes using index
        Args:
            args (list): list of the nre values
        '''
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
            return
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return

    def to_dictionary(self):
        '''returns a dictionary representation of a rectangle object
        '''
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        my_dict['width'] = self.width
        my_dict['height'] = self.height

        return (my_dict)

    def __str__(self):
        '''string representation of the instances'''

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
