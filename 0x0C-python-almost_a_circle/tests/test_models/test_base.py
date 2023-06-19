#!/usr/bin/python3
"""This module contains unit tests for the base.py module"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test cases for the Base class"""
    def test_1_id_a(self):
        """Test initialization when id is None"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_2_id_b(self):
        """Test initialization when id is an integer"""
        b3 = Base(234)
        b4 = Base(456)
        self.assertEqual(b3.id, 234)
        self.assertEqual(b4.id, 456)


if __name__ == "__main__":
    unittest.main()
