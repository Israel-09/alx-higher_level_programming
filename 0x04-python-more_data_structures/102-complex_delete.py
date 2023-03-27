#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if not a_dictionary or a_dictionary is None:
        return None
    key_list = list(a_dictionary.keys())
    for k in key_list:
        if a_dictionary.get(k) == value:
            del a_dictionary[k]
    return a_dictionary
