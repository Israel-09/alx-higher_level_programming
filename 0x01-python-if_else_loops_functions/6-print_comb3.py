#!/usr/bin/python3
for i in range(9):
    for j in range(i, 10):
        if i == j:
            continue
        print("{}{}".format(i, j), end='')
        if i < 8:
            print(", ", end='')
print()
