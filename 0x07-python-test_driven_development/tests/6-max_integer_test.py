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
    
    def test_max_str(self):
        self.assertEqual(max_integer['a', 'b', 'c'], 'c')

    def test_bool(self)
        self.assertRaise(TypeError, max_integer, [True, 2, 4])

    def test_3_int(self)
        self.assertEqual(max_integer[1, 4, 5], 5)

    def test_max_middle(self)
        self.assertEqual(max_integer[4, 55, 9], 55)

    def test_float(self)
        self.assertEqual(max_integer[22.3, 5, 7], 22)

    def test_neg(self)
        self.assertEqual(max_integer[-3, -22, -2], -2)

if __name__ == '__main__':
    unittest.main()
