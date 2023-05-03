import unittest
from rect import print_rectangle


class TestUppercase(unittest.TestCase):
    def test_print_rectangle(self):
        temp = print_rectangle(12, 4, '@')
        self.assertEqual(temp, [['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'], ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'], ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'], ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']])

    def test_print_rectangle_empty(self):
        temp = print_rectangle(0, 0, '*')
        self.assertEqual(temp, [])