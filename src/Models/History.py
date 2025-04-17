class History:
    def __init__(self, userID):
        self.userID=userID
        self.calculations = []

    def addEntry(self, calculation):
        self.calculations.append(calculation)

    def viewHistory(self):
        return self.calculations
    
    def clearHistory(self):
        self.calculations.clear()