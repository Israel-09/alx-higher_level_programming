#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    integers = 0
    i = 0
    while i < x:
        try:
            print('{:d}'.format(my_list[i]), end='')
            integers += 1
        except ValueError:
            pass
        except TypeError:
            pass
        i += 1
    print()
    return integers
