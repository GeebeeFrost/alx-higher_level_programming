#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the key with the biggest integer value"""
    if not a_dictionary:
        return None
    if len(a_dictionary) == 1:
        return list(a_dictionary.values())[0]
    return max(list(a_dictionary.values()))
