# Reflections for Object state modeling and activity workflow objective.
## 1. Challenges in Choosing Granularity for States/Actions

One of the main challenges in modeling was deciding the level of granularity. Too much detail makes diagrams cluttered and hard to follow, while too little detail risks missing important transitions or activities. For example, in the Advanced Calculator System, modeling every calculation type as a separate state/action made the diagrams too complex. To balance this, similar actions (like different types of unit conversions) were grouped under broader categories like “Perform Conversion” for simplicity and better readability.
## 2. Aligning Diagrams with Agile User Stories

Another challenge was mapping diagrams accurately to Agile user stories. Agile focuses on delivering small, incremental value through user-centric stories, which sometimes lacked the technical specificity needed for precise diagramming. For example, a user story like “As a user, I want to export my results” required interpreting what backend processes that entails (e.g., generating files, triggering downloads). Ensuring diagrams reflect this functionality without making assumptions required collaboration with stakeholders or clarification of acceptance criteria.
## 3. Comparing State Diagrams vs. Activity Diagrams

Aspect State Diagrams Activity Diagrams Focus Object behavior over time Step-by-step process flow Best for Lifecycle of a single object Modeling workflows and system processes Example Use Calculator session: Idle → Active → Closed Export workflow, registration, calculations Visual Elements States, transitions, events, guards Actions, decisions, concurrency, swimlanes Challenge Hard to model parallel actions Less suited for object-level behavior

Summary: State diagrams were ideal for showing how the calculator or user account changes states due to events (e.g., login, session expired), while activity diagrams effectively captured end-to-end workflows such as performing calculations or exporting results.
