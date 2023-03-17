#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    key_list = list(a_dictionary.keys())
    if len(key_list) == 0 and value >= len(key_list):
        return None
    for k in key_list:
        if a_dictionary.get(k) == value:
            del a_dictionary[k]
    return a_dictionary
