#!/usr/bin/python3
"""Uses GitHub API to display student's id using credentials"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth_header = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth_header)
    print(res.json().get("id"))
