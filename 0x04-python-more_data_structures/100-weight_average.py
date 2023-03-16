#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    for i in my_list:
        multiple = 1
        for j in i:
            multiple = multiple * j
        den += j
        num += multiple
    return num/den
