#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    s1 = Square(10, 2, 8)
    s2 = Square(4)
    Square.save_to_file([s1, s2])

    with open("Square.json", "r") as file:
        print(file.read())
