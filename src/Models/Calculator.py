class Calculator:
    def __init__(self, calculatorID, type):  # Use __init__ (double underscores)
        self.calculatorID = calculatorID
        self.type = type

    def calculateExpressions(self, expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def validateInput(self, expression):
        return isinstance(expression, str) and expression.strip() != ""
        
    def displayResults(self, result):  # Fixed typo: "displayReults" -> "displayResults"
        print(f"Result: {result}")
