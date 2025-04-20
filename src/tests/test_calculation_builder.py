from creational_patterns.Builders.calculation_builder import CalculationBuilder
import unittest

class TestCalculationBuilder(unittest.TestCase):
    def test_build_custom_calc(self):
        builder = CalculationBuilder()
        calc = builder.set_id("C001").set_expression("10 / 4").set_precision(2).build()
        
        # Perform the calculation
        calc.perform()  # Perform calculation, this will update the `result` attribute
        
        # Access the result from the `Calculation` object
        result = calc.result  # This accesses the `result` attribute which should now contain the calculated value
        
        # Now test the result
        self.assertAlmostEqual(result, 2.5, places=2)  # Check if the result is approximately 2.5
