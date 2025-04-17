from Models.Calculator import Calculator

class CalculatorFactory:
    @staticmethod
    def get_calculator(calculator_type):
        calculatorID = "Calc001"  # You can change this to a dynamic ID generation logic
        if calculator_type == "Basic":
            return Calculator(calculatorID, "Basic")
        elif calculator_type == "Scientific":
            return Calculator(calculatorID, "Scientific")
        elif calculator_type == "Graphing":
            return Calculator(calculatorID, "Graphing")
        else:
            raise ValueError("Invalid calculator type")
