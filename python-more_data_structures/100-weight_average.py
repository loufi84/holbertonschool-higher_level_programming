#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_w = sum(weight for value, weight in my_list)
    total_w_value = sum(value * weight for value, weight in my_list)

    return total_w_value / total_w
