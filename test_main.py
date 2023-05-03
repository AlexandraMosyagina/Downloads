import unittest
from add import add


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        result = add(5, 10)
        self.assertEqual(result, 15)

    def test_add_negative(self):
        result = add(-5, -10)
        self.assertEqual(result, -15)

    def test_add_negative_and_positive(self):
        result = add(-50, 20)
        self.assertEqual(result, -30)


if __name__ == 'main':
    unittest.main()
