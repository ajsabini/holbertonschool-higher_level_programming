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
        if attrs is None:
            return self.__dict__
        else:
            obj = {}
            for x in attrs:
                if x in self.__dict__.keys():
                    obj[x] = self.__dict__[x]
            return obj

    def reload_from_json(self, json):
        """"""
        for i in dict(self.__dict__):
            if i in json:
                self.__dict__[i] = json[i]
