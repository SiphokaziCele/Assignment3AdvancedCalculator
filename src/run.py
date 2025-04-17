import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Calculator factory')))

from Models.Calculator import Calculator
from CalculatorFactory import CalculatorFactory

if __name__ == "__main__":
    calc = CalculatorFactory.get_calculator("Basic")
    result = calc.calculate("5 + 5 * 2")
    print(f"Result: {result}")
