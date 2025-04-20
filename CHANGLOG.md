# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2025-04-20
### Added
- Implemented Singleton pattern for the Encryption Manager to ensure secure and consistent encryption handling.
- Added unit tests for Singleton instance validation.
- Export calculation history feature (US-008).
- Graphing mathematical functions (US-004).

### Fixed
- Corrected file structure by moving generated test reports into the `src` directory.
- Resolved issue with `pytest` not recognized by using `python -m pytest`.

---

## [1.0.0] - 2025-04-15
### Added
- Core calculator logic including arithmetic, trigonometric, and logarithmic functions.
- Calculation Builder pattern implementation.
- Factory pattern for calculator creation.
- Unit conversion feature (US-005).
- User story management using GitHub Projects.
- CI-ready test cases and coverage report integration.

