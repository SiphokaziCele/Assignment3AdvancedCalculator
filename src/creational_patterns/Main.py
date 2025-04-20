import sys
import os

# Add current script directory to the sys.path for importing
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # === Models === (only import if running this script directly, not when Models is its own main)
    try:
        from Models.User import User
        from Models.Calculations import Calculation
    except ImportError:
        print("Models import skipped. Running without Models.")
    
    # === Factories ===
    from creational_patterns.Factories.calculator_factory import CalculatorFactory
    from creational_patterns.Factories.results_formatter import PlainTextFormatter
    from creational_patterns.Factories.ui_factory import DarkThemeFactory

    # === Builders ===
    from creational_patterns.Builders.calculation_builder import CalculationBuilder

    # === Prototype ===
    from creational_patterns.Prototype.calculations_prototype import CalculationPrototype

    # === Singleton ===
    from creational_patterns.Singletons.logger import Logger

    print("🚀 Starting Advanced Calculator System...\n")

    # --- Logger (Singleton) ---
    logger = Logger()
    logger.log("Application launched")

    # --- Simple Factory ---
    calc = CalculatorFactory.get_calculator("Scientific")
    print("Factory Calculator Result:", calc.calculateExpressions("2 + 2 * 5"))


    # --- Factory Method ---
    formatter = PlainTextFormatter()
    print("Formatted Output:", formatter.format(20))

    # --- Abstract Factory ---
    theme = DarkThemeFactory()
    button = theme.create_button()
    label = theme.create_label()
    print(button.draw())
    print(label.render())

    # --- Builder Pattern ---
    builder = CalculationBuilder()
    custom_calc = builder.set_id("C1001").set_expression("10 / 3").set_precision(4).build()
    print("Builder Result:", custom_calc.perform())

    # --- Prototype ---
    original = CalculationPrototype("C001", "5 + 3", 8)
    copy = original.clone()
    copy.calc_id = "C002"
    print("Prototype Original:", original)
    print("Prototype Clone:", copy)

    # --- Logger logs ---
    print("\n📜 Logs:")
    for entry in logger.get_logs():
        print("→", entry)
