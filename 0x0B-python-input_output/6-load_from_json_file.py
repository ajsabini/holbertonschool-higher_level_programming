#!/usr/bin/python3
"""create an object from a json file"""


import json


def load_from_json_file(filename):
    """funtion that do the onversion, recieve the json file"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
