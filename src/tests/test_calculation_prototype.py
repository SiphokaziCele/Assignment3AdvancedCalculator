import unittest
from creational_patterns.Prototype.calculations_prototype import CalculationPrototype

class TestCalculationPrototype(unittest.TestCase):
    def test_clone(self):
        original = CalculationPrototype("C001", "3 + 3", 6)
        clone = original.clone()
        self.assertEqual(clone.result, 6)
        self.assertNotEqual(original.calc_id, "C002")
