#!/usr/bin/python3
def max_integer(my_list=[]):
    """Returns the biggest integer of a list"""
    if len(my_list) < 1:
        return None
    if len(my_list) == 1:
        return my_list[0]
    i, big = 0, 0
    while i < len(my_list) - 1:
        if my_list[i] > my_list[i + 1] and my_list[i] > big:
            big = my_list[i]
        elif my_list[i + 1] > big:
            big = my_list[i + 1]
        i += 1
    return big
