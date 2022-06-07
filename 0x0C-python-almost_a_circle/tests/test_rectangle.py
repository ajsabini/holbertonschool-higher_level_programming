#!/usr/bin/python3
"""Rectangle class - doing unittests"""

import io
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class for test Rectangle"""

    def test_pep8_base(self):
        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/rectangle.py'])
        self.AssertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )

if __name__ == '__main__':
    unittest.main()
