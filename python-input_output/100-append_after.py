#!/usr/bin/python3
'''

'''


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        lines = f.readlines()

    new_line = []
    for line in lines:
        new_line.append(line)
        if search_string in line:
            new_line.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(new_line)
