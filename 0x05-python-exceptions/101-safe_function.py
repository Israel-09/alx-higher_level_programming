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

def my_div(a, b):
        return a / b


result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))

def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))

