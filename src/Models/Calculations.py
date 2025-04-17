from datetime import datetime

class Calculation:
    def _init_ (self, calculationID, expression):
        self.calculationID= calculationID
        self.expression=expression
        self.result = None
        self.timestamp = datetime.now ()
       

    def perform (self):
        try:
            self.result= eval (self.expression)
        except Exception:
            self.result = "Error"
            return self.result
    
    def SaveToHistory(self):
        # user.add(self)
        print("Sure, Jan")