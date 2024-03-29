#!/usr/bin/python3
"""This script takes in a URL and displays the value of X-Request-Id header"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
