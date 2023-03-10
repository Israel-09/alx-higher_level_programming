#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1
    print("{} argument{}".format(ac, 's:'if ac > 1 else '.'))
    for i in range(ac + 1):
        if i > 0:
            print("{}: {}".format(i, argv[i]))
