#!/usr/bin/python3
"""
contains a python function that prints the
name of the user for a given input
Example:
    >>> say_my_name('John', 'Sam')
    My name is John Sam
"""


def say_my_name(first_name, last_name=""):
    import string
    """say_my_name prints the name of a user
    provided the input of the user

    Args:
        first_name (str):    user's first name
        last_name (str):     user's last name

    Raises:
        TypeError: if first_name or last_name is not string
    """
    if (
            type(first_name) is not str or first_name == "" or
            first_name.isalpha() is False
            ):
        raise TypeError("first_name must be a string")
    if (
            type(last_name) is not str or
            last_name.isalpha() is False and
            last_name != ''
            ):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
