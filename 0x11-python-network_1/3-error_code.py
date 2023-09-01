#!/usr/bin/python3
"""This script takes in a URL and displays error codes"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        try:
            print(response.read().decode("ascii"))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
