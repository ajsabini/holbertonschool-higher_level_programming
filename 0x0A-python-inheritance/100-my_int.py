#!/usr/bin/python3
"""module - subclass int"""


class MyInt(int):
    """def class"""

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
