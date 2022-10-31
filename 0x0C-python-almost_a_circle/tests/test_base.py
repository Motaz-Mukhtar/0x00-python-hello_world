#!/usr/bin/python3
"""Test for the Base Class on Base.py File"""
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
