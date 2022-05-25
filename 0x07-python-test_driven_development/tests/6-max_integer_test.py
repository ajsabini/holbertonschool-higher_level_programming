#!/usr/bin/python3
""""""

import unittest

class TestingMaxInteger(unittest.TestCase):

    def test_one_none(self):
        self.assertRaises(TypeError, max_integer, [None, 4, 6])

    def test_all_none(self):
        self.assertRaises(TypeError, max_integer, [None, None, None])

    def test_one_str(self):
        self.assertRaises(TypeError, max_integer, [23, "canfla", 9])

if __name__ == '__main__':
    unittest.main()
