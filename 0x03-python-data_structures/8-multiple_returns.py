#!/usr/bin/python3
def multiple_returns(sentence):
    res = len(sentence), "{}".format(None if not sentence else sentence[0])
    return res
