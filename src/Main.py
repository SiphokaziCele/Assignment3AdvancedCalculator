from User import User
from Calculator import Calculator
from Calculations import Calculation

user = User("u01", "Sisipho", "sisi@example.com", "1234")
user.login()

calc = Calculator("c01", "Basic")
expression = "5 + 3 * 2"
if calc.validate_input(expression):
    result = calc.calculate_expression(expression)
    calc.display_result(result)

    c = Calculation("calc01", expression)
    c.perform()
    c.save_to_history(user)

    print([f"{calc.expression} = {calc.result}" for calc in user.history.view_history()])
