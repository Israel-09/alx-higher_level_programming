#!/usr/bin/python3
for i in range(100):
    print("{}{}".format(i, ", " if i < 99 else ''), end='')
print()
