#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase"""
    caps = ""
    for c in str:
        if ord(c) in range(97, 123):
            caps += "{}".format(chr(ord(c) - 32))
        else:
            caps += "{}".format(c)
    print("{}".format(caps))
