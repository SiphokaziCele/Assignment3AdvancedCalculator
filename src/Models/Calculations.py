from datetime import datetime

class Calculation:
    def __init__(self, calculationID, expression, precision=2, rounding=True):
        self.calculationID= calculationID
        self.expression=expression
        self.result = None
        self.timestamp = datetime.now ()
        self.precision = precision  # New attribute for precision
        self.rounding = rounding  
       

    def perform (self):
        try:
            self.result= eval (self.expression)
        except Exception:
            self.result = "Error"
            return self.result
    
    def SaveToHistory(self):
        # user.add(self)
        print("Sure, Jan")