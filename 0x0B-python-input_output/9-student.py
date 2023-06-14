#!/usr/bin/python3
'''
module on file io
in python
'''


class Student:
    '''defination of a student class'''
    def __init__(self, first_name, last_name, age):
        '''
        constructor for student class
        Args:
            first_name(str):    student's first name.
            last_name(str):     student's last name.
            age (int):          student's age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)
