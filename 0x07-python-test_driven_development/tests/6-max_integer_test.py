#!/usr/bin/python3
""""""

import unittest

class TestingMaxInteger(unittest.TestCase):

    def test_none(self):
        self.assertRaises(TypeError, max_integer, [None, 4, 6])

if __name__ == '__main__':
    unittest.main()
