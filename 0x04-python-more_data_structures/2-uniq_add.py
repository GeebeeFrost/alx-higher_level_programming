#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    nums = set(my_list)
    res = 0
    for i in nums:
        res += i
    return res
