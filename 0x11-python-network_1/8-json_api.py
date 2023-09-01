#!/usr/bin/python3
"""Takes a letter and sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) < 2 else sys.argv[1]
    body = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=body)
    try:
        response = res.json()
        if not response:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
