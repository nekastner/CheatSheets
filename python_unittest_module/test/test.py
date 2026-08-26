import unittest
import sys

sys.path.insert(0, "../src")
from src import calculator

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(calculator.add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(calculator.add(1, -2), -1)
        self.assertEqual(calculator.add(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()