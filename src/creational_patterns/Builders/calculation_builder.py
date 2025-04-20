#--Builder--#

from Models.Calculations import Calculation

class CalculationBuilder:
    def __init__(self):
        self.calculation_id = None
        self.expression = ""
        self.precision = 2
        self.rounding = True

    def set_id(self, calc_id):
        self.calculation_id = calc_id
        return self

    def set_expression(self, expr):
        self.expression = expr
        return self

    def set_precision(self, precision):
        self.precision = precision
        return self

    def disable_rounding(self):
        self.rounding = False
        return self

    def build(self):
        # Return an instance of the Calculation class instead of CustomCalculation
        return Calculation(
            self.calculation_id,
            self.expression,
            self.precision,
            self.rounding
        )
