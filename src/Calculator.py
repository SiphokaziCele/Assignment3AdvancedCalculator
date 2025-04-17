class Calculator:
    def _init_ (self, calculatorID, type):
        self.calculatorID= calculatorID
        self.type=type
       

    def calculateExpressions (self, expression):
        try:
            result= eval (expression)
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def validateInput(self, expression):
        return isinstance(expression, str) and expression.strip() !=""
        
    def displayReults(self, result):
        print (f"result: {result}")