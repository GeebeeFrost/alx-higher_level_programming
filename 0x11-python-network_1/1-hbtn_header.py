#!/usr/bin/python3
"""This script takes a URL and
displays the value of the X-Request-Id variable"""
import sys
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
