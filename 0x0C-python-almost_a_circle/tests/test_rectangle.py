#!/usr/bin/python3
"""Test for the Base Class on Base.py File"""
import unittest
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        re1 = Rectangle(3, 0)
        re2 = Rectangle(5, 9)
        re3 = Rectangle(10, 0, 0, 2, 20)
        self.assertEqual(re1.id, re2.id - 1)
        self.assertEqual(re2.id, 2)
        self.assertEqual(re3.id, 20)
        self.assertEqual(re3.width, 10)
    
    def test_area(self):
        r1 = Rectangle(20, 15)
        r2 = Rectangle(2, 10, 1, 1)
        self.assertEqual(r1.area(), r1.__width * r1.__height)
        self.assertEqual(r2.area(), r2.__width * r2.__height)

    
if __name__ == "__main__":
    unittest.main()