#!/usr/bin/python3
from math import pi


class MagicClass:
    def __init__(self, radius):
        """defines the attribute of a MagicClass object

        Args:
            radius: radius of the object

        Raise:
            Exception TypeError: if raius is not a number
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area defines the area occupied by a MagicClass object

        Returns:
            The area of a MagicClass Object
        """
        return (pi * (self.__radius ** 2))

    def circumference(self):
        """circumference defines the distance round a MagicClass object

        Returns:
            The circumference of a MagicClass Object
        """
        return (2 * pi * self.__radius)
