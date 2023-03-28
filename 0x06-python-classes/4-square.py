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

    def area(self):
        """
        area: calculates the area of a square

        Returns:
            The area of the sqaure
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        size(getter): returns the value of attribute size
        size(Setter): sets the value of size to new size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
