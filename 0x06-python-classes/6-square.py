#!/usr/bin/python3
"""module to create a square class"""


class Square:
    """a class that defines a square"""
    def __init__(self, size=0, position=(0,0)):
        """
        __init__: initializes the   properties of a square object

        Args:
            size: size of the square
        """
        self.__size = size
        self.__position = position

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
    
    @property
    def position(self):
        """
        position(getter): returns the value of attribute position
        position(Setter): sets the value of size to new positon
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """
        area: calculates the area of a square

        Returns:
            The area of the sqaure
        """
        return self.__size ** 2

    def my_print(self):
        """prints a suare using #"""
        ssize = self.__size
        space_cnt = self.__position[0]
        if self.__position[1] > 1:
            space_cnt = 0
        if ssize == 0:
            print()
        else:
            for i in range(ssize):
                for k in range(space_cnt):
                    print(' ', end='')
                for j in range(ssize):
                    print('{}'.format('#'), end='')
                print()
