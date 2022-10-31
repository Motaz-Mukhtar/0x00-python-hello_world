#!/usr/bin/python3
"""Test for square.py file in Square class"""
import sys
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_attributes(self):
        self.assertEqual(Square(2, 2), 5)

if __name__ == "__main__":
    unittest.main()