#!/usr/bin/python3
"""This script takes a URL, sends a POST request with an email and
displays the body of the response"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    var = {"email": sys.argv[2]}
    body = urllib.parse.urlencode(var).encode("ascii")
    req = urllib.request.Request(sys.argv[1], body)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
