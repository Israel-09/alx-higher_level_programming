#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    c = 0
    try:
        c = fct(args[0], args[1])

    except (ValueError, TypeError) as me:
        sys.stderr.write('Exception: ' + str(me) + '\n')
        c = None

    except ZeroDivisionError as me:
        c = None
        sys.stderr.write('Exception: ' + str(me) + '\n')

    except IndexError as me:
        c = None
        sys.stderr.write('Exception: ' + str(me) + '\n')

    return c
