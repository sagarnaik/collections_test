import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Test Case 1: Addition
    def test_addition(self):
        result = self.calculator.add(3, 4)
        self.assertEqual(result, 7)

    # Test Case 2: Subtraction
    def test_subtraction(self):
        result = self.calculator.subtract(8, 5)
        self.assertEqual(result, 3)

    # Test Case 3: Multiplication
    def test_multiplication(self):
        result = self.calculator.multiply(2, 6)
        self.assertEqual(result, 12)

    # Test Case 4: Division
    def test_division(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

    # Test Case 5: Division by zero should raise an exception
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

    # Test Case 6: Exponentiation
    def test_exponentiation(self):
        result = self.calculator.power(2, 3)
        self.assertEqual(result, 8)

    # Test Case 7: Square root
    def test_square_root(self):
        result = self.calculator.sqrt(9)
        self.assertEqual(result, 3)

    # Test Case 8: Absolute value
    def test_absolute_value(self):
        result = self.calculator.abs_value(-5)
        self.assertEqual(result, 5)

    # Test Case 9: Check if the calculator instance is created
    def test_calculator_instance(self):
        self.assertIsInstance(self.calculator, Calculator)

    # Test Case 10: Verify subtraction result for negative numbers
    def test_subtraction_negative_result(self):
        result = self.calculator.subtract(5, 8)
        self.assertEqual(result, -3)

if __name__ == '__main__':
    unittest.main()
