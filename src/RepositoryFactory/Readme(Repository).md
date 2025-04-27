## Dependency Management Approach

For this project, a **Factory Pattern** approach was chosen instead of full **Dependency Injection (DI)**.

### Reason for Choosing Factory Pattern:

- The system is relatively small and focused.
- Factory allows **dynamic object creation** (e.g., choosing between `InMemoryUserRepository` and `FileSystemUserRepository`) without needing a large DI framework.
- Factory keeps the design **simple and understandable** while still supporting future scalability.
- DI frameworks (e.g., in Java/Spring) are more suitable for **large, complex systems** with hundreds of dependencies.

---

### Summary:

- A `/factories` directory was created.
- `RepositoryFactory` dynamically instantiates the correct repository type (`MEMORY` or `FILE`).
- This keeps the code **modular**, **scalable**, and **easy to extend**.

  If the system grows bigger, adding a proper **Dependency Injection Container** would be the next step.
