# Activity Workflow Modeling for Calculator System
## 1.User Registration
``` mermaid
graph TD;
    A(Start) --> B(User enters details)
    B --> C(Validate Input)
    C -- Invalid Data --> D(Show Error Message)
    D --> B
    C -- Valid Data --> E(Create Account)
    E --> F(Send Confirmation Email)
    F --> G(Account Activated)
    G --> H(End)
```
### Explanation
Stakeholder Concern: Ensures users can not create duplicate or invalid accounts.

Parallel Actions: Sends confirmation email after successful registration.
