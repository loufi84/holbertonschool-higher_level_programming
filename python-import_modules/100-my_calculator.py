#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    result = 0
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        sys.exit(1)
    if sys.argv[2] == '+':
        result = add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '-':
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '*':
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '/':
        result = div(int(sys.argv[1]), int(sys.argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /", end="\n")
        sys.exit(1)
    print("{:d}".format(result), end="\n")
