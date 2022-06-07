#!/usr/bin/python3
"""doing unittest for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout
import pycodestyle

class BaseTest(unittest.TestCase):
    """test for Base class"""

    def test_pep8_base(self):
        """checks PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )
