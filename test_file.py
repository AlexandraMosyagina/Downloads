import unittest
from file import uppercase


class TestUppercase(unittest.TestCase):
    def test_uppercase(self):
        temp = uppercase(['lololol', 'nya', 'omg'])
        self.assertEqual(temp, ['LOLOLOL', 'NYA', 'OMG'])

    def test_uppercase_empty(self):
        temp = uppercase([])
        self.assertEqual(temp, [])