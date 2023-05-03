import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    def setUp(self):
        self.object1 = Fraction(5, 10)
        self.object2 = Fraction(3, 9)

    def test_add(self):
        self.assertEqual(self.object1.__add__(self.object2), '75 / 90')

    def test_subtraction(self):
        self.assertEqual(self.object1.__add__(self.object2), '75 / 90')