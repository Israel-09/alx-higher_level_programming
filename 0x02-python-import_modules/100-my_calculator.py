#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv as av

    if len(av) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(av[1])
    b = int(av[3])
    sign = av[2]
    if sign == '+':
        print("{} {} {} = {}".format(a, sign, b, add(a, b)))
    elif sign == '-':
        print("{} {} {} = {}".format(a, sign, b, sub(a, b)))
    elif sign == '*':
        print("{} {} {} = {}".format(a, sign, b, mul(a, b)))
    elif sign == '/':
        print("{} {} {} = {}".format(a, sign, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
