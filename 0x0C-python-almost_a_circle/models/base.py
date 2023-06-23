#!/usr/bin/python3
'''module of a python base class'''


class Base:
    '''class of a base models'''

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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation
        of list_dictionary

        Args:
            list_dictionary (list): is alist of dictionary

        Returns:
            return the JSON representaion of list_dictionary
        '''
        from json import dumps

        if list_dictionaries:
            return dumps(list_dictionaries)
        else:
            return dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        '''saves list objects to a file
        Args:
            list_objs: is a list of instances who inherits of Base
        '''

        storage = f'{cls.__name__}.json'

        list_dictionaries = []
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            list_dictionaries.append(obj_dict)

        str_dict = Base.to_json_string(list_dictionaries)

        with open(storage, 'w', encoding='utf-8') as f:
            f.write(str_dict)
