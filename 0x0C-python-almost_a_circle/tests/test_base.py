#!/usr/bin/python3
# test_base.py
"""Test for the Base Class on Base.py File"""
import sys
# sys.path.insert(1, "C:/Users/admin/Desktop/taifoor jalon/alx-higher_level_programming/0x0C-python-almost_a_circle")
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_attributes(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertAlmostEqual(b1.id, 1)
        self.assertAlmostEqual(b2.id, 2)
        self.assertAlmostEqual(b3.id, 12)

if __name__ == "__main__":
    unittest.main()