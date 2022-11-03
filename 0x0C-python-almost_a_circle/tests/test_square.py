#!/usr/bin/python3
"""Test for square.py file in Square class"""
import sys
import io
# sys.path.insert(1, "/root/alx-higher_level_programming/0x0C-python-almost_a_circle")
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_attributes(self):
        r1 = Square(5, 1)
        r2 = Square(9, 6)
        r3 = Square(2, 2)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.id, r3.id - 1)
        self.assertEqual(r3.width, 2)

    def test_raises(self):
        with self.assertRaises(TypeError):
            Square("4", 4)
        with self.assertRaises(ValueError):
            Square(0, 0)
    
    def test_area(self):
        self.assertEqual(Square(2).area(), 2 * 2)
        self.assertEqual(Square(10).area(), 10 * 10)
        self.assertEqual(Square(50).area(), 50 * 50)
    
    def test_str(self):
        string = "[Square] (4) 2/3 - 1"
        r1 = Square(1, 2, 3, 4)
        self.assertEqual(str(r1), string)
    
    def test_to_dictionary_method(self):
        r1 = Square(2, 5, 6, 10)
        dictionary = {
            "id": 10,
            "x": 5,
            "size": 2,
            "y": 6,
        }
        self.assertEqual(r1.to_dictionary(), dictionary)
    
    def test_update_args_method(self):
        r1 = Square(3, 1, 0, 51)
        r1.update(45, 10, 5, 1)
        r1_string = "[Square] (45) 5/1 - 10"
        self.assertEqual(str(r1), r1_string)

    def test_update_kwargs_method(self):
        r1 = Square(9, 2, 4, 76)
        dictionary = {
            "id": 99,
            "x": 2,
            "size": 8,
            "y": 8,
        }
        r1_string = "[Square] (99) 2/8 - 8"
        r1.update(**dictionary)
        self.assertEqual(str(r1), r1_string)



class TestStdout_Square (unittest.TestCase):
    @staticmethod
    def capture_stdout(square, method):
        """Capture and return the stdout of 
            the moethod
            
            Args:
                square (Square): Square Class
                method (str): Square method
            
            Returns:
                text printed in stdout
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(square)
        else:
            square.display()
        sys.stdout = sys.__stdout__
        return capture
    
    def test_print_method(self):
        r1 = Square(5, 1, 0, 90)
        cap = TestStdout_Square.capture_stdout(r1, "print")
        string = "[Square] (90) 1/0 - 5\n"
        self.assertEqual(cap.getvalue(), string)
    
    def test_display_method(self):
        r1 = Square(3)
        cap = TestStdout_Square.capture_stdout(r1, "display")
        self.assertEqual(cap.getvalue(), '###\n###\n###\n')
    
    def test_display_x_y_method(self):
        r1 = Square(2, 2, 2, 2)
        cap = TestStdout_Square.capture_stdout(r1, "display")
        self.assertEqual(cap.getvalue(), '\n\n  ##\n  ##\n')

if __name__ == "__main__":
    unittest.main()










# '\n\n  ###\n  ###\n  ###\n'
# '\n\n  ###\n  ###\n'