#!/usr/bin/python3
"""Test for the Base Class on Base.py File"""
import unittest
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        re1 = Rectangle(3, 0)
        re2 = Rectangle(5, 9)
        re3 = Rectangle(10, 0, 0, 2, 20)
        self.assertEqual(re1.id, 1)
        self.assertEqual(re2.id, 2)
        self.assertEqual(re3.id, 20)
        self.assertEqual(re3.width, 10)

if __name__ == "__main__":
    unittest.main()