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
        if type(width) is not int and type(height) is not int:
            raise TypeError("size must be an integer")
        if width < 0 and height < 0:
            raise ValueError("size must be >= 0")
        self.__width = width
        self.__height = height

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def print_rect(self):
        """creates a string representing
        the shape of a rectangle"""
        rectangle = ''
        if self.__height == 0 or self.__width == 0:
            return rectangle
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += '#'
            if i < self.__height - 1:
                rectangle += '\n'
        return rectangle

    def __str__(self):
        """string representations of a rectangle object
        Return:
            The string representaion of the rectangle object
        """
        return (self.print_rect())
