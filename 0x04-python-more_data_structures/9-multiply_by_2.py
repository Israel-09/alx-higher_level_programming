#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    keys = new_dict.keys()

    for k in new_dict:
        new_dict[k] = new_dict.get(k) * 2

    return new_dict
