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
        self.__size = size
