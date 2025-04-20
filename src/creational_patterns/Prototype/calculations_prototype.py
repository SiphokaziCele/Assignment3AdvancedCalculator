import copy

class CalculationPrototype:
    def __init__(self, calc_id, expression, result):
        self.calc_id = calc_id
        self.expression = expression
        self.result = result

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"[{self.calc_id}] {self.expression} = {self.result}"
