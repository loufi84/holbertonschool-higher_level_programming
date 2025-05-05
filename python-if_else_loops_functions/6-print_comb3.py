#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        print("{:02d}, ".format(i * 10 + j) if i != 8 or j != 9
              else "{:02d}\n".format(i * 10 + j), end="")
