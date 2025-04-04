### Advanced Calculator System: Activity Diagrams & Explanations (GitHub-Ready Mermaid Format)
---

## 1. **User Registration Workflow**

```mermaid
flowchart TD
    subgraph User
        A1(Start) --> A2[Enter Details]
    end

    subgraph System
        A2 --> B1[Validate Input]
        B1 -->|Invalid| B2[Show Error Message]
        B2 --> A2
        B1 -->|Valid| C1[Create Account]
        C1 --> C2[Send Confirmation Email]
        C2 --> D1(End)
    end
```

**Explanation:**
- This workflow shows how users register.
- Decision node checks if input is valid.
- If valid, system proceeds with creation and email.
- Addresses stakeholder need for secure sign-up.
- Stakeholder Concern: Ensuring that user registrations are secure and validated.

How It Addresses the Concern: The system first validates the user's input, ensuring that only valid data is accepted. If the input is invalid, an error message is displayed, prompting the user to correct the details. Once the input is valid, the account is created, and a confirmation email is sent to the user. This addresses concerns regarding secure sign-up and proper validation of user information.

## 2. **Login Workflow**

```mermaid
flowchart TD
    subgraph User
        A1(Start) --> A2[Enter Credentials]
    end

    subgraph System
        A2 --> B1[Authenticate User]
        B1 -->|Failed| B2[Display Login Error]
        B2 --> A2
        B1 -->|Success| C1[Redirect to Dashboard]
        C1 --> D1(End)
    end
```

**Explanation:**
- Shows how login is handled.
- Branching logic validates credentials.
- Addresses security concern from users.
- Stakeholder Concern: Ensuring that only authenticated users can access the system.

How It Addresses the Concern: The login process involves checking the user’s credentials. If the credentials are valid, the system grants access by redirecting the user to their dashboard. If the credentials are incorrect, an error is displayed, ensuring that unauthorized access is prevented. This addresses security concerns for both users and administrators.

---

## 3. **Perform Calculation**

```mermaid
flowchart TD
    subgraph User
        A1(Start) --> A2[Enter Expression]
    end

    subgraph System
        A2 --> B1[Parse Input]
        B1 --> B2[Validate Expression]
        B2 -->|Invalid| B3[Display Error]
        B3 --> A2
        B2 -->|Valid| C1[Evaluate Expression]
        C1 --> D1[Display Result]
        D1 --> E1(End)
    end
```

**Explanation:**
- Core calculator logic.
- Ensures expressions are valid before evaluation.
- Functional link: FR-001 (Basic Calculations).
-Stakeholder Concern: Ensuring that the calculator performs accurate and error-free calculations.

How It Addresses the Concern: The system first parses and validates the user’s input. If the expression is invalid, an error message is displayed, prompting the user to enter a valid expression. If the input is valid, the expression is evaluated, and the result is displayed. This ensures that the calculator performs accurate calculations and handles errors effectively, meeting the functional requirements for basic calculations.
---

## 4. **Graphing Calculator Workflow**

```mermaid
flowchart TD
    subgraph User
        A1(Start) --> A2[Input Function]
    end

    subgraph System
        A2 --> B1[Parse Function]
        B1 --> B2[Generate Plot Data]
        B2 --> B3[Render Graph]
        B3 --> C1(End)
    end
```

**Explanation:**
- Visualizes the advanced graphing feature.
- Related to US-004 (Graphing).
- Stakeholder Concern: Providing an advanced graphing feature for users.

How It Addresses the Concern: This workflow demonstrates how the graphing feature works. The user inputs a mathematical function, which is then parsed and used to generate plot data. The system then renders the graph, providing a visual representation of the function. This workflow fulfills the need for advanced features like graphing, which appeals to users needing visualizations in their calculations.

---

## 5. **Save Calculation History**

```mermaid
flowchart TD
    subgraph System
        A1(Start) --> A2[Check History Enabled]
        A2 -->|Disabled| B1(End)
        A2 -->|Enabled| C1[Store Result in DB]
        C1 --> D1(End)
    end
```

**Explanation:**
- Stores user calculations if enabled.
- Addresses FR-003 (History Logging).
- Stakeholder Concern: Providing users with a way to track their past calculations.

How It Addresses the Concern: If the user has enabled history logging, the system will store the result of each calculation in a database, allowing the user to review their past calculations. If history logging is disabled, the process ends without storing any data. This addresses the need for users to have a record of their past calculations, enhancing usability.

---

## 6. **Export History Workflow**

```mermaid
flowchart TD
    A1([Start]) --> A2[User clicks Export Button]
    A2 --> B1[System generates file - PDF or CSV]
    B1 --> C1[System triggers download]
    C1 --> D1([End])


```

**Explanation:**
- Enables data portability.
- Fulfills FR-008 (Export History).
- Stakeholder Concern: Allowing users to export their calculation history for offline use.

How It Addresses the Concern: This workflow enables the user to export their calculation history in a format such as PDF or CSV. The system generates the file and triggers the download, ensuring users can keep records of their calculations. This feature addresses the need for portability and usability, particularly for users who want to keep a history of their work for future reference.

---

## 7. **Unit Conversion Workflow**

```mermaid
flowchart TD
    subgraph User
        A1(Start) --> A2[Enter Value & Units]
    end

    subgraph System
        A2 --> B1[Lookup Conversion Formula]
        B1 --> B2[Perform Conversion]
        B2 --> C1[Display Result]
        C1 --> D1(End)
    end
```

**Explanation:**
- Provides a unit converter.
- Functional mapping to US-005.
- Stakeholder Concern: Providing users with a way to convert units easily.

How It Addresses the Concern: The system allows users to enter a value and specify the units they want to convert. It then looks up the appropriate conversion formula and performs the conversion, displaying the result. This workflow addresses the need for a simple and accurate unit conversion tool, ensuring that users can easily convert values across various units.

---

## 8. **Encryption Option Workflow**

```mermaid
flowchart TD
    subgraph User
        A1(Start) --> A2[Enable Encryption in Settings]
    end

    subgraph System
        A2 --> B1[Apply Encryption to Stored Data]
        B1 --> C1(End)
    end
```

**Explanation:**
- Secures user data.
- Matches US-009 (Data Encryption).
- Stakeholder Concern: Ensuring user data is secure and encrypted.

How It Addresses the Concern: This workflow addresses data security by allowing users to enable encryption through the settings. Once enabled, the system encrypts any stored data, ensuring it is protected from unauthorized access. This feature enhances user trust and ensures compliance with security best practices.

---

