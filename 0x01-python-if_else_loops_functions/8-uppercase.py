#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = ord(str[i])
        if c >= ord('a') and c <= ord('z'):
            c -= 32
        print('{}'.format(chr(c)), end='')
    print()
