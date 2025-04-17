from Models.Calculator import Calculator


class CalculatorFactory:
    @staticmethod
    def get_calculator(calculator_type):
        if calculator_type == "Basic":
            return Calculator("Basic")
        elif calculator_type == "Scientific":
            return Calculator("Scientific")
        elif calculator_type == "Graphing":
            return Calculator("Graphing")
        else:
            raise ValueError("Invalid calculator type")
