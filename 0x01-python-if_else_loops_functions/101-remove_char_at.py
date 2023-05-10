#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    elif n == 0:
        return str[1:]
    else:
        result = str[:n] + str[(n + 1):]
        return result
