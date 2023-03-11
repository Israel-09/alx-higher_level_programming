#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    s_list = []
    for i in my_string:
        if i == 'C' or i == 'c':
            continue
        s_list.append(i)
    return new_str.join(s_list)
