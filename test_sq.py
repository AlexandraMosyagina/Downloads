import unittest
from sq import count_area


class TestUppercase(unittest.TestCase):
    def test_count_area(self):
        temp = count_area(10)
        self.assertEqual(temp, 100)

    def test_count_area_negative(self):
        temp = count_area(-20)
        self.assertEqual(temp, 40)