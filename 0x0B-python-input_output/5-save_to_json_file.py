#!/usr/bin/python3
"""write an obj to a tet file, using JSON repres"""


import json


def save_to_json_file(my_obj, filename):
    """function recieve obj and filename"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
