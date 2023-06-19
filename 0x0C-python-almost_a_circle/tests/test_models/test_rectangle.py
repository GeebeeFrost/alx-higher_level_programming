#!/usr/bin/python3
"""This module contains unit test cases for the rectangle.py module"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test cases for the Rectangle class"""
    def setUp(self):
        """Test set-up"""
        self.r1 = Rectangle(10, 2)

    def tearDown(self):
        """Test tidying"""
        del self.r1

    def test_1_width_height(self):
        """Test when width and height are integers"""
        self.assertEqual(self.r1.id, 3)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.width, 10)

    def test_2_x_y(self):
        """Test when x and y are integers"""
        self.r1.x = 2
        self.r1.y = 4
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 4)

    def test_3_width_height(self):
        """Test when width and height are not integers or <= 0"""
        with self.assertRaises(TypeError):
            self.r1.width = [1, 2]
            self.r1.height = (3)
        with self.assertRaises(ValueError):
            self.r1.width = -2
            self.r1.height = 0

    def test_4_x_y(self):
        """Test when x and y are not integers or less than or equal to 0"""
        with self.assertRaises(TypeError):
            self.r1.x = [1, 2]
            self.r1.y = (3)
        with self.assertRaises(ValueError):
            self.r1.x = -2
            self.r1.y = -3


if __name__ == "__main__":
    unittest.main()
