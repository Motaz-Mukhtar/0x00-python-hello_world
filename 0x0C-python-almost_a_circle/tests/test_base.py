#!/usr/bin/python3
# test_base.py
"""Test for the Base Class on Base.py File"""
import sys
import json
# sys.path.insert(1, "C:/Users/admin/Desktop/taifoor jalon/alx-higher_level_programming/0x0C-python-almost_a_circle")
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def test_attributes(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        self.assertAlmostEqual(b1.id, 1)
        self.assertAlmostEqual(b2.id, 2)
        self.assertAlmostEqual(b3.id, 12)

    def test_to_json_string_method(self):
        r1 = Rectangle(5, 1, 2, 10)
        r2 = Rectangle(2, 20)
        dictionary1 = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        string1 = json.dumps([dictionary1])
        string2 = json.dumps([dictionary2])
        self.assertEqual(Base.to_json_string([dictionary1]), string1)
        self.assertEqual(Base.to_json_string([dictionary2]), string2)
        self.assertEqual(Base.to_json_string([]), "[]")
    
    # def test_from_json_string(self):
    #     r1 = Rectangle(5, 20, 10, 9)
    #     r2 = Rectangle(10, 2, 2, 5)
    #     list_of_obj = r1.to_dictionary()
    #     string = json.dumps(list_of_obj)
    #     self.assertEqual(Base.from_json_string(), list_of_obj)

    def test_create_method(self):
        r1 = Rectangle(5, 1, 2, 19)
        dictionary = {"width": 5, "height": 1, "x": 2, "y": 19}
        r2 = Base.create(r1, **dictionary)
        self.assertEqual(r1, r2)

    # def test_load_from_file_method(self):
        




if __name__ == "__main__":
    unittest.main()
