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
---
## Language Choice: Python

    Why Python?
    Python was selected due to its simplicity, readability, and strong community support. It allowed for quick development of both core
    calculator logic and unit testing using built-in and third-party libraries.

### Key benefits:

        Ease of prototyping – Ideal for testing out design ideas quickly.

        Rich standard library – Modules like math, unittest, and external ones like pytest made testing and implementation seamless.

        Cross-platform compatibility – Works on Windows, Mac, and Linux, making the app widely accessible.

        Clear syntax – Encourages clean, readable, and maintainable code.

## Key Design Decisions

### Modular Architecture

        Code is separated into logical modules:

            calc_logic.py: Core logic.

            formatter.py: Responsible for formatting outputs.

            logger.py: Handles system logging.

            ui_factory.py & calculator_factory.py: Implements Factory pattern for UI and calculator type creation.

    Why? Improves maintainability, scalability, and testing.

### Design Patterns

        Singleton Pattern used in logger.py:

            Ensures only one instance of the logger is used throughout the application.

            Prevents duplicate or inconsistent logs.

        Factory Pattern used in calculator_factory.py:

            Decouples object creation from logic.

            Makes it easier to add new calculator types without modifying existing code.

### Test-Driven Development (TDD)

        Tests were written using pytest before or alongside implementation.

        Coverage tools ensured code was well-tested.

        🧪 Ensured reliability and made debugging easier.

### User Stories → Code

        The project follows user-centric requirements, for example:

            Graphing functions (matplotlib)

            Saving frequently used calculations

            Exporting history

            Performing unit conversions

        Each feature maps directly to a user story on the backlog.

### Security Consideration

        In user data features (planned or implemented), encryption is considered for secure handling of sensitive data.
## Links to the codes
###  `src/` Directory Overview

## 📁 Key Project Folders and Files

- [**src/Models/**](https://github.com/SiphokaziCele/Assignment3AdvancedCalculator/tree/main/src/Models)  
  Contains data structures and logic models used in calculator operations.

- [**src/creational_patterns/**](https://github.com/SiphokaziCele/Assignment3AdvancedCalculator/tree/main/src/creational_patterns)  
  Implements common creational design patterns like Singleton, Factory, and Builder.

- [**src/tests/**](https://github.com/SiphokaziCele/Assignment3AdvancedCalculator/tree/main/src/tests)  
  Unit tests for validating each component of the application.

- [**src/test_results.txt**](https://github.com/SiphokaziCele/Assignment3AdvancedCalculator/blob/main/src/test_results.txt)  
  Output log of test results generated by pytest.

  ## Assignment 11

### Links to the code:
[**src/Repositories/**](https://github.com/SiphokaziCele/Assignment3AdvancedCalculator/tree/main/src/Repositories)
Contains all repository-related classes and interfaces.  
  Includes: **Repository<T, ID>** (generic interface), **UserRepository**, **InMemoryUserRepository**, and **JSON_Repo** for saving and retrieving user data.

[**src/RepositoryFactory/**](https://github.com/SiphokaziCele/Assignment3AdvancedCalculator/tree/main/src/RepositoryFactory)
Contains the **RepositoryFactory** class.  
  This factory dynamically creates the correct repository instance (either memory-based or file-based) at runtime based on the selected storage type.
  
[**src/UpdatedClassDiagram.md/**](https://github.com/SiphokaziCele/Assignment3AdvancedCalculator/tree/main/src/UpdatedClassDiagram.md)
Contains the updated UML Class Diagram (using Mermaid) showing both the original system models and the newly added repository layer with interfaces and implementations.

# ✅ Assignment 12 Summary: User Registration Feature

## 📌 Overview
This assignment implements a **User Registration Feature** using layered architecture. The components include:

- Service Layer for business logic
- REST API endpoints using FastAPI
- FastAPI application with Swagger documentation
- Unit tests for service logic

---

## 📁 Project Structure & Locations

### 1. 🧠 User Registration Service Layer
- **Purpose**: Contains core business logic for registering users.
- **File**: [src/services/user_service.py](https://github.com/SiphokaziCele/Assignment3AdvancedCalculator/tree/main/src/services/user_service.py)
- **Functionality**:
  - register_user(user_data: dict): Validates and stores a new user
- **Dependencies**: Relies on `UserRepository` for user data operations.

---

### 2. 🌐 REST API Endpoints
- **Purpose**: Exposes HTTP endpoints for user registration via FastAPI.
- **File**: [`src/api/user_routes.py`](https://github.com/SiphokaziCele/Assignment3AdvancedCalculator/tree/main/src/api/user_routes.py)
- **Base Route**: `/api/users`

#### Endpoints
| Method | Route | Description |
|--------|-------|-------------|
| POST   | `/api/users/register` | Register a new user |

**Example request (JSON):**
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123"
}





