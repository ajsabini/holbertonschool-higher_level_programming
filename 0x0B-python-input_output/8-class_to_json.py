#!/usr/bin/python3
"""
    module - return the dictionary w/simple data
    for json serialize of an object
"""


def class_to_json(obj):
    """function recieve an obj and return a dit(json serialize)"""
    return obj.__dict__
