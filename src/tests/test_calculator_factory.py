
import unittest
from creational_patterns.Factories.calculator_factory import CalculatorFactory

class TestCalculatorFactory(unittest.TestCase):
    def test_scientific_calculator(self):
        calc = CalculatorFactory.get_calculator("Scientific")
        self.assertEqual(calc.calculateExpressions("2 + 3 * 2"), 8)

    def test_invalid_type_raises(self):
        with self.assertRaises(ValueError):
            CalculatorFactory.get_calculator("Alien")
