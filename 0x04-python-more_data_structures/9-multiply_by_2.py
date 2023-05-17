#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns new dictionary with values multiplied by 2"""
    res = {key: a_dictionary[key] * 2 for key in list(a_dictionary)}
    return res
