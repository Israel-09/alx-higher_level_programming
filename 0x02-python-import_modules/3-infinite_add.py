#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    count = 0
    for i in range(len(argv)):
        if i > 0:
            count = count + int(argv[i])
    print("{}".format(count))
