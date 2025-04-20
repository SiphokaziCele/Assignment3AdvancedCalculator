import unittest
from Models.Calculator import Calculator

class TestCalculatorLogic(unittest.TestCase):

    def test_addition(self):
        calc = Calculator("c01","Basic")
        result = calc.calculateExpressions("2 + 3")
        self.assertEqual(result, 5)

    def test_multiplication_precedence(self):
        calc = Calculator("c01", "Basic")
        result = calc.calculateExpressions("2 + 3 * 4")
        self.assertEqual(result, 14)  # 3*4=12 + 2 = 14

    def test_parentheses(self):
        calc = Calculator("c01", "Basic")
        result = calc.calculateExpressions("(2 + 3) * 4")
        self.assertEqual(result, 20)

    def test_invalid_expression(self):
        calc = Calculator("c01","Basic")
        result = calc.calculateExpressions("5 + ")
        self.assertTrue("Error" in str(result))

    def test_division_by_zero(self):
        calc = Calculator("c01","Basic")
        result = calc.calculateExpressions("10 / 0")
        self.assertTrue("Error" in str(result))

if __name__ == '__main__':
    unittest.main()
