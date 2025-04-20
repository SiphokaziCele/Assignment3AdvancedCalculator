## Implemented Patterns & Justifications
### 1. Simple Factory Pattern

    Used For: Creating different types of calculators (Basic, Scientific, Graphing).

    Why: Centralizes object creation based on type. Simplifies how external components request calculators.

    Class: CalculatorFactory

    Location: Factories/calculator_factory.py

### 2. Factory Method Pattern

    Used For: Formatting results in different styles.

    Why: Allows result formatting to be extended (e.g., JSON, plain text) without modifying the formatter logic.

    Classes: ResultFormatter (abstract), PlainTextFormatter, JsonFormatter

    Location: Factories/results_formatter.py

### 3. Abstract Factory Pattern

    Used For: Generating UI components (buttons and labels) for light and dark themes.

    Why: Provides an interface to create families of related objects without specifying their concrete classes.

    Classes: UIFactory, DarkThemeFactory, LightThemeFactory, DarkButton, LightButton, etc.

    Location: Factories/ui_factory.py

### 4. Builder Pattern

    Used For: Building complex Calculation objects with optional attributes like rounding and precision.

    Why: Offers a step-by-step approach to constructing objects with multiple configuration options.

    Class: CalculationBuilder

    Location: Builders/calculation_builder.py

### 5. Prototype Pattern

    Used For: Cloning calculation objects to avoid re-initializing them from scratch.

    Why: Enables efficient duplication of objects with the same state and structure.

    Class: CalculationPrototype

    Location: Prototype/calculations_prototype.py

### 6. Singleton Pattern

    Used For: Central logging service.

    Why: Ensures a single global logger instance throughout the application.

    Class: Logger

    Location: Singletons/logger.py
