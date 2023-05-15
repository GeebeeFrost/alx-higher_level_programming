#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position"""
    if my_list:
        cop = my_list[:]
        if idx < 0 or idx >= len(my_list):
            return cop
        cop[idx] = element
        return cop
