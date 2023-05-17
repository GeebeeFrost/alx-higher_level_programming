#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the key with the biggest integer value"""
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 1:
        return list(a_dictionary.keys())[0]
    highest = max(list(a_dictionary.values()))
    for k, v in a_dictionary.items():
        if v == highest:
            return k
