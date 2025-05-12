#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    res = []
    for i in range(list_length):
        try:
            if i >= len(my_list1) or i >= len(my_list2):
                raise IndexError
            if (not isinstance(my_list1[i], (int, float)) or
                    not isinstance(my_list2[i], (int, float))):
                raise TypeError
            if my_list2[i] == 0:
                raise ZeroDivisionError

            res.append(my_list1[i] / my_list2[i])

        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
        except TypeError:
            print("wrong type")
            res.append(0)
        except IndexError:
            print("out of range")
            res.append(0)
        finally:
            pass
    return res
