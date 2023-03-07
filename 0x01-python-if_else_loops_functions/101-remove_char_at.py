#!/usr/bin/python3
def remove_char_at(str, n):
    list = []
    for i in range(len(str)):
        if i == n:
            continue
        list.append(str[i])
    return ''.join(list)
