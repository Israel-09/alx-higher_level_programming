#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 3))
try:
    my_square_2.position = (2, 4, 6)
    my_square_2.size = 8

    print(my_square_2.position)
    print(my_square_2.size)
except Exception as me:
    print(me)

my_square_2.my_print()

print("--")

my_square_3 = Square(3, ('goog', 0))
my_square_3.my_print()

print("--")
