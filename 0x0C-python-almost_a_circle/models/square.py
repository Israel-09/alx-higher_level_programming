#!/usr/bin/python3
'''python module on square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''a square class that inherits from rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''class constructor fro square class'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''returns the value of size'''
        return self.width

    @size.setter
    def size(self, value):
        '''changes the value of size
        Args:
            value (int): the new value of size
        '''
        self.width = value
        self.height = value

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
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for k,v in kwargs.items():
                setattr(self, k, v)
    
    def __str__(self):
        '''string representation of square class'''
        return '[square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                self.width)
