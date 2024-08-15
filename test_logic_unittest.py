# test_logic_unittest.py
import unittest
from logic import CalculatorActions


class TestCalculatorActions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(CalculatorActions.add_numbers(1, 2), 3)
        self.assertEqual(CalculatorActions.add_numbers(-1, 1), 0)
        self.assertEqual(CalculatorActions.add_numbers(-1, -1), -2)
        self.assertEqual(CalculatorActions.add_numbers(0, 0), 0)

    def test_subtract_numbers(self):
        self.assertEqual(CalculatorActions.subtract_numbers(10, 5), 5)
        self.assertEqual(CalculatorActions.subtract_numbers(0, 0), 0)
        self.assertEqual(CalculatorActions.subtract_numbers(-1, -1), 0)
        self.assertEqual(CalculatorActions.subtract_numbers(-1, 1), -2)

    def test_multiply_numbers(self):
        self.assertEqual(CalculatorActions.multiply_numbers(3, 4), 12)
        self.assertEqual(CalculatorActions.multiply_numbers(-1, 1), -1)
        self.assertEqual(CalculatorActions.multiply_numbers(0, 5), 0)
        self.assertEqual(CalculatorActions.multiply_numbers(-2, -3), 6)


if __name__ == '__main__':
    unittest.main()
