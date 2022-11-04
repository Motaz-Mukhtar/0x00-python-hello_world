#!/usr/bin/python3
# test_rectangle.py
"""Test for the Rectangle Class on rectangle.py File"""
import sys
import io
# sys.path.insert(1, "/root/alx-higher_level_programming/0x0C-python-almost_a_circle")
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

    def test_str(self):
        string = "[Rectangle] (50) 3/4 - 1/2"
        r1 = Rectangle(1, 2, 3, 4, 50)
        self.assertEqual(str(r1), string)
    
    def test_to_dictionary_method(self):
        r1 = Rectangle(2, 5, 6, 7, 10)
        dictionary = {
            "x": 6,
            "y": 7,
            "id": 10,
            "height": 5,
            "width": 2
        }
        self.assertEqual(r1.to_dictionary(), dictionary)
    
    def test_update_args_method(self):
        r1 = Rectangle(3, 1, 0, 0, 51)
        r1.update(45, 10, 5, 1, 1)
        r1_string = "[Rectangle] (45) 1/1 - 10/5"
        self.assertEqual(str(r1), r1_string)

    def test_update_kwargs_method(self):
        r1 = Rectangle(9, 2, 4, 10, 76)
        dictionary = {
            "id": 99,
            "width": 2,
            "height": 8,
            "x": 8,
            "y": 9
        }
        r1_string = "[Rectangle] (99) 8/9 - 2/8"
        r1.update(**dictionary)
        self.assertEqual(str(r1), r1_string)


class TestStdout_Rectangle (unittest.TestCase):
    @staticmethod
    def capture_stdout(rect, method):
        """Capture and return the stdout of 
            the moethod
            
            Args:
                rect (Rectangle): Rectangle Class
                method (str): Rectangle method
            
            Returns:
                text printed in stdout
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture
    
    def test_print_method(self):
        r1 = Rectangle(5, 1, 0, 0, 9)
        cap = TestStdout_Rectangle.capture_stdout(r1, "print")
        string = "[Rectangle] (9) 0/0 - 5/1\n"
        self.assertEqual(cap.getvalue(), string)
    
    def test_display_method(self):
        r1 = Rectangle(5,2)
        cap = TestStdout_Rectangle.capture_stdout(r1, "displya")
        self.assertEqual(cap.getvalue(), '#####\n#####\n')
    
    def test_display_x_y_method(self):
        r1 = Rectangle(3, 2, 2, 2)
        cap = TestStdout_Rectangle.capture_stdout(r1, "display")
        self.assertEqual(cap.getvalue(), '\n\n  ###\n  ###\n')

if __name__ == "__main__":
    unittest.main()

