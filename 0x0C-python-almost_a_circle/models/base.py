#!/usr/bin/python3
'''module of a python base class'''


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        '''class constructor

        Args:
            id (int): unique ID for each object
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
