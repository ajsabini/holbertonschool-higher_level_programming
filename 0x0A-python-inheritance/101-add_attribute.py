#!/usr/bin/python
"""add attribut to an obj"""


def add_attribute(mc, name, other):
    """the funtion"""
    if hasattr(mc, '__dict__'):
        setattr(mc, name, other)
    else:
        raise TypeError("can't add new attribute")
