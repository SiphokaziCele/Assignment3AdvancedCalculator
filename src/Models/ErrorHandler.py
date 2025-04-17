class ErrorHanndler:
    def _init_(self):
        self.errorCode = None
        self.errorMessage = None

    def catchInputError(self, expression):
        if not expression:
            self.errorCode = "ERR001"
            self.errorMessage = "Invalid input"
            self.logError()

    def logError(self):
        print(f"Error [{self.errorCode}]: {self.errorMessage}")