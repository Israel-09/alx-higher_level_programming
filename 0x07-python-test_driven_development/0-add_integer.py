#!/usr/bin/python3
"""module of math operations
sums up the value of two integers
>>> add_integer(6, 6)
12
"""


def add_integer(a, b=98):
    """sums up two numbers

    Args:
        a: first number
        b: second number

    Return:
        The sum of a and b

    Raises:
        TypeError: if either a or b is neither an integer
            nor float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    result = a + b
    return (result)
