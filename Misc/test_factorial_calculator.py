import unittest
from factorial_calculator import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_integer(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_of_large_number(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_with_negative_input(self):
        with self.assertRaises(RecursionError):
            factorial(-1)

if __name__ == "__main__":
    unittest.main()