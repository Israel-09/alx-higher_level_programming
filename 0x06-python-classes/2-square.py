#!/usr/bin/python3
"""module to create a square class"""


class Square:
    """a class that defines a square"""
    def __init__(self, size=0):
        """
        __init__: initializes the properties of a square object

        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
