#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(roman_string)):
        if i > 0 and conv[roman_string[i]] > conv[roman_string[i - 1]]:
            res += conv[roman_string[i]] - 2 * conv[roman_string[i - 1]]
        else:
            res += conv[roman_string[i]]
    return res
