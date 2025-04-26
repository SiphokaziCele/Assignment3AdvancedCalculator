import sys
import os

# Add current script directory to the sys.path for importing
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # === Models ===
    try:
        from Models.User import User
        from Models.Calculations import Calculation
    except ImportError:
        print("Models import skipped. Running without Models.")
    
    # === Creational Patterns ===
    from creational_patterns.Factories.calculator_factory import CalculatorFactory
    from creational_patterns.Factories.results_formatter import PlainTextFormatter
    from creational_patterns.Factories.ui_factory import DarkThemeFactory
    from creational_patterns.Builders.calculation_builder import CalculationBuilder
    from creational_patterns.Prototype.calculations_prototype import CalculationPrototype
    from creational_patterns.Singletons.logger import Logger

    print("🚀 Starting Advanced Calculator System...\n")

    # --- Singleton: Logger ---
    logger = Logger()
    logger.log("Application launched")

    # --- Simple Factory ---
    calc = CalculatorFactory.get_calculator("Scientific")
    print("🧮 Factory Calculator Result:", calc.calculateExpressions("2 + 2 * 5"))

    # --- Factory Method ---
    formatter = PlainTextFormatter()
    print("📝 Formatted Output:", formatter.format(20))

    # --- Abstract Factory ---
    theme = DarkThemeFactory()
    button = theme.create_button()
    label = theme.create_label()
    print("🎨 UI Elements:")
    print(button.draw())
    print(label.render())

    # --- Builder Pattern ---
    builder = CalculationBuilder()
    custom_calc = builder.set_id("C1001").set_expression("10 / 3").set_precision(4).build()
    print("🧱 Builder Result:", custom_calc.perform())

    # --- Prototype Pattern ---
    original = CalculationPrototype("C001", "5 + 3", 8)
    copy = original.clone()
    copy.calc_id = "C002"
    print("🧬 Prototype Original:", original)
    print("🧬 Prototype Clone:", copy)

    # --- Logger logs ---
    print("\n📜 Logger Logs:")
    for entry in logger.get_logs():
        print("→", entry)

    # === Assignment 11: Repository Layer Test ===
    print("\n💾 Testing Repository Layer (Assignment 11)")

    from RepositoryFactory.repository_factory import RepositoryFactory

    # Choose storage type: "MEMORY" or "FILE"
    storage_type = "FILE"  # or change to "MEMORY" to use InMemoryUserRepository

    user_repo = RepositoryFactory.get_user_repository(storage_type)

    # Save a user
    user = User("U011", "Sisipho Repo", "repo@example.com", "secure123")
    user_repo.save(user)
    print("✅ User saved to", storage_type, "repository.")

    # Retrieve user
    retrieved = user_repo.find_by_id("U011")
    if retrieved:
        print(f"🔍 Retrieved: {retrieved.name} ({retrieved.email})")

    # List all users
    users = user_repo.find_all()
    print("📋 All Users in Repo:")
    for u in users:
        print("→", u.name)

    # Delete the user
    user_repo.delete("U011")
    print("🗑️ User deleted.")

    # Confirm deletion
    if not user_repo.find_by_id("U011"):
        print("✅ Deletion confirmed.")
