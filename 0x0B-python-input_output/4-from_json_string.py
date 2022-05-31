#!/usr/bin/python3
"""return an obj python represented by a JSON str"""


import json


def from_json_string(my_str):
    """function recieve a my_str"""
    return json.loads(my_str)
