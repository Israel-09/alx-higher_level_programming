#!/usr/bin/python3

def uniq_add(my_list=[]):
    a = set(my_list)
    total = 0
    for i in a:
        total += i
    return total
