#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another"""
    replaced = my_list[:]
    for i in range(len(replaced)):
        if replaced[i] == search:
            replaced[i] = replace
    return replaced
