#!/usr/bin/python3
for i in range(122, 96, -1):
    print('{}'.format(chr(i) if i%2 != 1 else chr(i - 32)), end='')
