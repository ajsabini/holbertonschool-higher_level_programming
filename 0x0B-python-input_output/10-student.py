#!/usr/bin/python3
"""module - class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """init the obj th class, fn, ln, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function that return a dict of a Student instance"""
        if type(attrs) is not list or attrs is None:
            return self.__dict__
        for elem in attrs:
            if type(elem) is not str:
                return self.__dict__
        else:
                obj = {}
                obj = self.__dict__
                for key, value in obj.items():
                    for elem in attrs:
                        if elem == key:
                            obj.update({key: value})
                return obj
