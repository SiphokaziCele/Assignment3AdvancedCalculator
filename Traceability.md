
# Traceability
## For activity Diagrams
The following section shows how each diagram relates to the functional requirements and user stories:

### 1. **User Registration Workflow**
- **Functional Requirements (Assignment 4):**
  - FR-002: User must be able to register by entering their details, and the system must validate the input before creating an account.
- **User Stories (Assignment 6):**
  - US-001: As a user, I want to create an account by entering my details so that I can access the advanced calculator system.
- **Sprint Task:**
  - Implement the user registration form, including input validation and confirmation email.
- **Diagram Explanation:**
  - This diagram shows the user registration process. It validates input and ensures users are registered securely. This addresses stakeholder needs for a secure sign-up process.

---

### 2. **Login Workflow**
- **Functional Requirements (Assignment 4):**
  - FR-001: Users must be able to log in to access the system securely.
- **User Stories (Assignment 6):**
  - US-002: As a user, I want to log in using my credentials so that I can access my personalized dashboard.
- **Sprint Task:**
  - Implement login functionality with authentication and error handling.
- **Diagram Explanation:**
  - This workflow illustrates the login process, ensuring that users can only access the system with valid credentials. It ensures security as per the functional requirements.

---

### 3. **Perform Calculation Workflow**
- **Functional Requirements (Assignment 4):**
  - FR-001: The system must allow the user to input a mathematical expression and display the result.
  - FR-004: The system must ensure that the input is a valid expression before evaluation.
- **User Stories (Assignment 6):**
  - US-003: As a user, I want to enter an expression and get the result so that I can perform basic calculations.
- **Sprint Task:**
  - Implement input parsing and expression validation for the calculator.
- **Diagram Explanation:**
  - The core calculation logic is demonstrated here, validating the input and ensuring only valid expressions are evaluated. This fulfills the functional requirement for basic calculations.

---

### 4. **Graphing Calculator Workflow**
- **Functional Requirements (Assignment 4):**
  - FR-005: The system must provide the ability to input a mathematical function and generate a graphical representation of it.
- **User Stories (Assignment 6):**
  - US-004: As a user, I want to input a function and see its graph so that I can visualize the relationship between variables.
- **Sprint Task:**
  - Implement the graphing functionality, including function parsing
---
### 5.Save Calculation History Workflow
- **Functional Requirements (Assignment 4):**
    - FR-006: The system must allow users to save and access a history of their previous calculations.
- **User Stories (Assignment 6):**
    -  US-005: As a user, I want to be able to view my calculation history so that I can track what I’ve done before.
- **Sprint Task:**
    - Implement a backend history feature and connect it to the user interface.
---
### 6. Export Results Workflow
- **Functional Requirements (Assignment 4):**
    - FR-007: The system must allow users to export calculation results as a PDF or CSV.
- **User Stories (Assignment 6):**
    -  US-006: As a user, I want to download my results in a readable format so that I can share or store them.
 - **Sprint Task:**
     - Implement export functionality using file generation libraries.
---
### 7. Unit Conversion Workflow

  - **Functional Requirements (Assignment 4):**
    - FR-008: The system must provide the ability to convert between different units (e.g., length, weight, temperature).

 - **User Stories (Assignment 6):**
     - US-007: As a user, I want to convert between different units so that I can complete everyday or academic tasks more efficiently.

  - **Sprint Task:**
    -  Implement unit selection, conversion logic, and error handling.
---
### 8. Advanced Functions Workflow (Trigonometry, Logarithms, etc.)

  - **Functional Requirements (Assignment 4):**
    - FR-009: The system must support advanced mathematical functions including trigonometry, logarithms, and powers.

 - **User Stories (Assignment 6):**
   -  US-008: As a user, I want to perform complex scientific calculations so that I can use the tool for academic purposes.

 - **Sprint Task:**
   - Implement advanced function parsing and integrate with the core calculation engine.
## For State Transition diagrams
### 1. User Account

- **Functional Requirements (Assignment 4):**
    - **FR-003:** Allow users to delete their accounts.
    - **FR-007:** Admin can suspend accounts for violations.
  
- **User Stories (Assignment 6):**
    - **US-002:** As a user, I want to verify my account to activate it.
    - **US-003:** As an admin, I want to suspend user accounts that violate the rules.
    - **US-004:** As an admin, I want to delete user accounts when necessary.

- **Sprint Task:**
    - Implement account suspension and deletion functionality for admins.
    - Implement email verification for users to activate their accounts.

---

### 2. Calculation Process

- **Functional Requirements (Assignment 4):**
    - **FR-010:** Perform calculations efficiently.
  
- **User Stories (Assignment 6):**
    - **US-006:** As a user, I want to select an operation to start a calculation.
    - **US-007:** As a user, I want to view the result of the calculation after the system processes it.

- **Sprint Task:**
    - Implement a calculation feature that processes the input and returns results efficiently.
    - Ensure smooth transition between calculation steps (from idle to computing to displaying results).

---

### 3. History Recorded

- **Functional Requirements (Assignment 4):**
    - **FR-015:** Allow users to save calculations to view later.
  
- **User Stories (Assignment 6):**
    - **US-005:** As a user, I want to save my calculations so I can view them later.
    - **US-008:** As a user, I want to delete my saved calculations if they are no longer needed.

- **Sprint Task:**
    - Implement functionality to save and delete calculation history.
    - Develop a user interface for displaying saved calculations.

---

### 4. Graphing Function

- **Functional Requirements (Assignment 4):**
    - **FR-020:** Provide graphing capabilities.

- **User Stories (Assignment 6):**
    - **US-010:** As a user, I want to generate a graph from my data so I can visualize the results.
    - **US-011:** As a user, I want to view the graph once it has been generated.

- **Sprint Task:**
    - Implement the graphing functionality to process data and generate graphs.
    - Develop the interface to display the generated graph to the user.

---

### 5. Unit Conversion

- **Functional Requirements (Assignment 4):**
    - **FR-025:** Enable unit conversions.

- **User Stories (Assignment 6):**
    - **US-012:** As a user, I want to convert between different units.
    - **US-013:** As a user, I want to see the result of my unit conversion.

- **Sprint Task:**
    - Implement unit conversion functionality for various units.
    - Create a user interface to display the conversion results.

---

### 6. Session Management

- **Functional Requirements (Assignment 4):**
    - **FR-030:** Auto-logout after inactivity.

- **User Stories (Assignment 6):**
    - **US-014:** As a user, I want the system to log me out after inactivity for security.
    - **US-015:** As a user, I want to manually log out from the system.

- **Sprint Task:**
    - Implement automatic logout feature after a specified time of inactivity.
    - Implement a manual logout option for users.

---

### 7. Setting Configuration

- **Functional Requirements (Assignment 4):**
    - **FR-035:** Allow users to personalize settings.

- **User Stories (Assignment 6):**
    - **US-016:** As a user, I want to customize my settings to match my preferences.
    - **US-017:** As a user, I want to reset my settings to the default values.

- **Sprint Task:**
    - Implement user settings customization options.
    - Provide the ability to reset settings to their default values.
