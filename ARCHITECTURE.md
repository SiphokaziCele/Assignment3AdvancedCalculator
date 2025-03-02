```mermaid
erDiagram
    USER ||--o{ CALCULATION : performs
    USER ||--o{ HISTORY : stores
    CALCULATION ||--|{ FUNCTION : uses
    HISTORY }|..|{ CALCULATION : references
