#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    sorted_keys = sorted(a_dictionary)

    for k in sorted_keys:
        print("{}: {}".format(k, a_dictionary[k]))
