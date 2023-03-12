#!/usr/bin/python3

def add_tuple(tuple_a=(0, 0), tuple_b=(0, 0)):
    a = [0, 0]
    b = [0, 0]

    if tuple_a:
        i = 0
        while (i < len(tuple_a) and i < 2):
            a[i] = tuple_a[i]
            i += 1
    if tuple_b:
        i = 0
        while (i < len(tuple_b) and i < 2):
            b[i] = tuple_b[i]
            i += 1
    first = a[0] + b[0]
    second = a[1] + b[1]
    return first, second

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
