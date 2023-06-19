#!/usr/bin/python3
"""This module contains unit test cases for the rectangle.py module"""
from models.rectangle import Rectangle
import unittest
from unittest.mock import patch
from io import StringIO
import sys


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

    def test_5_area(self):
        """Test area function"""
        self.r1.width = 10
        self.r1.height = 2
        self.assertEqual(self.r1.area(), 20)

    def test_6_display(self):
        """Test display function"""
        with self.assertRaises(TypeError):
            self.r1.display(1)
            self.r1.display([2, 3], "dsd")
            self.r1.display({34})
            self.r1.display((4, 5))

    def test_7_str(self):
        """Test magic __str__ function"""
        exOutput = "[Rectangle] ({}) {}/{} - {}/{}".format(self.r1.id,
                                                           self.r1.x,
                                                           self.r1.y,
                                                           self.r1.width,
                                                           self.r1.height)
        self.assertEqual(str(self.r1), exOutput)


if __name__ == "__main__":
    unittest.main()
