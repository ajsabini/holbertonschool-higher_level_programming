#!/usr/bin/python3
"""class for inherits"""


class MyList(list):
    """list class"""

    def print_sorted(self):
        """prit list, ascending sort"""
        sorted_list = sorted(self)
        print(sorted_list)
