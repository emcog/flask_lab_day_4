import unittest
from modules.calculator import *

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(10, add(5,5))

    def test_subtract(self):
        self.assertEqual(0, subtract(10,10))

    def test_divide(self):
        self.assertEqual(1, divide(10,10))

    def test_multiply(self):
        self.assertEqual(100, multiply(10,10))