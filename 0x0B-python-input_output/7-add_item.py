#!/usr/bin/python3
"""This script adds arguments to a Python list and serializes to a file"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    ls = sys.argv[1:]
    try:
        items = load("add_item.json")
    except Exception:
        save(ls, "add_item.json")
    else:
        for arg in ls:
            items.append(arg)
        save(items, "add_item.json")
