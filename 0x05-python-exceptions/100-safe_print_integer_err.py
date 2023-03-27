#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except ValueError as me:
        sys.stderr.write(str(me) + '\n')
        return False
    except TypeError as me:
        sys.stderr.write(str(me) + '\n')
        return False
