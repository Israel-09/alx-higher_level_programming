#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_list = list(a_dictionary.keys())
    max_score = a_dictionary.get(key_list[0])
    for k in key_list:
        if not a_dictionary[k]:
            return None
        if a_dictionary[k] > max_score:
            max_score = a_dictionary[k]
            max_key = k
    return max_key
