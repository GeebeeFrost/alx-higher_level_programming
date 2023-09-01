#!/usr/bin/python3
"""Takes in a URL, sends a POST request with an email to it and
displays the response"""
import requests
import sys

if __name__ == "__main__":
    var = {"email": sys.argv[2]}
    res = requests.post(sys.argv[1], data=var)
    print(res.text)
