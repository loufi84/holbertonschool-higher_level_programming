#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.", end="\n")
    else:
        if len(sys.argv) == 2:
            print("1 argument:", end="\n")
            print("1: {}".format(sys.argv[1]), end="\n")
        else:
            print("{} arguments:".format(len(sys.argv) - 1), end="\n")
            for i in range(1, len(sys.argv)):
                print("{:d}: {}".format(i, sys.argv[i]), end="\n")
