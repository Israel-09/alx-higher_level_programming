#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])

    except (ValueError, TypeError) as me:
        sys.stderr.write('Exception: ' + str(me) + '\n')
        result = None

    except ZeroDivisionError as me:
        result = None
        sys.stderr.write('Exception: ' + str(me) + '\n')

    except IndexError as me:
        result = None
        sys.stderr.write('Exception: ' + str(me) + '\n')
    return result
