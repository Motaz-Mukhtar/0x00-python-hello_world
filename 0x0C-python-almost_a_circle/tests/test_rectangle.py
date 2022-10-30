#!/usr/bin/python3
# test_rectangle.py
"""Test for the Rectangle Class on rectangle.py File"""
import sys
from unittest.case import _AssertRaisesContext
# sys.path.insert(1, "C:/Users/admin/Desktop/taifoor jalon/alx-higher_level_programming/0x0C-python-almost_a_circle")
import unittest
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        r1 = Rectangle(5, 1)
        r2 = Rectangle(9, 6)
        r3 = Rectangle(2, 2)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.id, r3.id - 1)
        self.assertEqual(r3.width, 2)
    def test_raises(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(TypeError):
            Rectangle(2, "4", "2", "1")
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 0, 0)
    
    def test_area(self):
        self.assertEqual(Rectangle(2, 5).area(), 2 * 5)
        self.assertEqual(Rectangle(10, 20).area(), 10 * 20)
        self.assertEqual(Rectangle(50, 10).area(), 50 * 10)
    
    def test_display(self):
        self.assertEqual(Rectangle(2, 2).display(), "##\n##")
if __name__ == "__main__":
    unittest.main()