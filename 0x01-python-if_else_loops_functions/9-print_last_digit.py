#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number - int(number/10) * 10
    if last_digit < 0:
        last_digit = last_digit * -1
    print("{}".format(last_digit), end='')
    return(last_digit)
