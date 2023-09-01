#!/usr/bin/python3
"""Takes in a URL, sends a request to it and displays the response
or error code if there is error"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
