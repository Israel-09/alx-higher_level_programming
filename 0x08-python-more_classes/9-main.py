#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(7)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(dir(my_square))
print(my_square)
