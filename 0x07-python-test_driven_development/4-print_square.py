#!/usr/bin/python3
"""
contains module to print a sqaure
for a given size
Example:
    >>> print_square(2)
    ##
    ##
"""


def print_square(size):
    """
    print_square prints a square for a given
    size using '#'.

    Args:
        size (int): the size of the square.

    Raises:
        TypeError:  if size is not an integer.
        ValueError: if size less than 0 and is float.
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
