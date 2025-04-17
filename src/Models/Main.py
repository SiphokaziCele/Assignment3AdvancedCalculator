from User import User
from Calculator import Calculator
from Calculations import Calculation

# Step 1: Create a user and log them in
user = User("u01", "Siphokazi", "sisi@example.com", "1234")
user.login()

# Step 2: Create a Calculator instance and validate input
calc = Calculator("c01", "Basic")
expression = "5 + 3 * 2"  # Example expression
if calc.validateInput(expression):
    result = calc.calculateExpressions(expression)
    calc.displayResults(result)

    # Step 3: Create a Calculation object and perform the calculation
    # c = Calculation("calc01", expression)
    c = Calculation()
    c.perform()  # Perform the calculation
    c.SaveToHistory()  # Save the result to the user's history

    # Step 4: View the history
    print([f"{calc.expression} = {calc.result}" for calc in user.history.viewHistory()])
