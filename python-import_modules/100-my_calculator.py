#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    result = 0
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == chr(43):
        result = add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, result), end="\n")
    elif op == chr(45):
        result = sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, result), end="\n")
    elif op == chr(42):
        result = mul(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, result), end="\n")
    elif op == chr(47):
        result = div(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, result), end="\n")
    else:
        print("Unknown operator. Available operators: +, -, * and /", end="\n")
        exit(1)
