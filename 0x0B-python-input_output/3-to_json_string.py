#!/usr/bin/python3
"""module - return json repr via obj"""


import json


def to_json_string(my_obj):
    """function that repr obj to a json"""
    return json.dumps(my_obj)
