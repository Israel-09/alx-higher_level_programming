#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(0, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(0, (3, -6))
my_square_3.position = (3, -5)
my_square_3.my_print()
print("--")

