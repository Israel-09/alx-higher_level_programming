#!/usr/bin/python3
"""module to create a square class"""


class Rectangle:
    """a class that defines a square"""
    def __init__(self, width=0, height=0):
        """
        __init__: initializes the properties of a square object

        Args:
            size: size of the square
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if type(height) is not int:
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        """
        width(getter): returns the value of attribute width
        width(Setter): sets the value of size to new width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height(getter): returns the value of attribute height
        height(Setter): sets the value of size to new height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
