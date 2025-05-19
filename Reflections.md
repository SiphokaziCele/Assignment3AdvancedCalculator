## Reflection: Balancing Stakeholder Needs

Developing the Advanced Calculator System involved balancing the needs of different groups, each with their own priorities. One of the main challenges was finding the right balance between simplicity and advanced features. Students and casual users wanted an easy-to-use interface, while researchers and professionals needed more complex functions like logarithms and graphing. To solve this, I created two modes: a simple one for everyday calculations and a more advanced one for technical tasks.

Security and performance were also a concern. The IT team wanted to make sure the system kept data safe, while users cared about how fast the system worked. To address both, I used strong encryption to protect sensitive data, while also ensuring calculations were completed quickly, in less than two seconds.

Another challenge was making the system work well on different devices and handle a lot of users at once. To do this, I designed the system to adjust to different screen sizes and organized the backend so it could manage many requests at the same time.

In the end, the project showed me how important it is to keep improving the system based on feedback. By building the system in a flexible way, I made sure it could be easily updated in the future while keeping it simple, secure, and fast.

# **Reflection: Challenges in Translating Requirements to Use Cases & Tests**

Translating stakeholder requirements into use cases and test cases posed several challenges in ensuring that all functional and non-functional aspects of the Advanced Calculator System were properly covered. One key difficulty was ensuring completeness—making sure that each stakeholder concern was properly addressed in a relevant use case. While the functional requirements from Assignment 4 provided a strong foundation, defining clear preconditions, postconditions, and alternative flows required deeper analysis of how users interact with the system. Every requirement had to be carefully scrutinized to ensure that it was not only reflected in the system design but also captured in the use cases and corresponding test cases.

Another challenge was handling complex interactions between different use cases. Some use cases, such as Perform Calculation and View History, were straightforward, but others, like Graphing a Function or Exporting History, involved multiple steps and dependencies. These use cases often had a cascade effect—one action would trigger another, and it was crucial to identify and map these interactions. Ensuring that these use cases remained modular while still supporting the overall system flow was essential. For instance, the Graph Function use case required seamless integration with Advanced Functions, where users would need to access more sophisticated mathematical features. Similarly, Export History not only relied on the data in View History but also involved exporting the data in a usable format. Managing such complex interactions without introducing confusion or redundancy was one of the key challenges in both the design and testing stages.

For test cases, mapping functional requirements to concrete validation steps was critical. Writing clear expected results for each test case required thinking about not only normal user behavior but also edge cases and error conditions. Non-functional tests, such as performance under high load or security validation, were particularly challenging, as they required consideration of real-world constraints like response time and encryption mechanisms. Testing for security was also complicated, given the sensitive nature of personal data that might be processed, making it essential to test for potential vulnerabilities and ensure that all transactions were encrypted and protected.

Finally, the balance between simplicity and usability was a recurring challenge. While the system needed to support advanced mathematical functions, it also had to remain accessible to general users. This required iterative adjustments to the use cases and test cases to refine error handling, accessibility, and performance considerations. The user interface needed to be intuitive, ensuring that both novices and advanced users could interact with the system effectively. In this process, feedback from stakeholders played a crucial role in fine-tuning the design to meet their expectations while maintaining a high level of functionality.

Overall, this process reinforced the importance of structured requirement analysis, iterative design, and comprehensive testing to ensure a robust and user-friendly system.

# Reflection: Challenges in Prioritization, Estimation, and Aligning Agile with Stakeholder Needs.

One of the most difficult aspects was determining which features should be implemented first. With no external stakeholders to validate decisions, I had to rely on my judgment and technical feasibility assessments. Initially, it was tempting to work on the more complex and visually appealing features, such as graphing (US-004), rather than the core calculator functions (US-001). However, prioritizing based on MoSCoW principles helped bring clarity, ensuring that basic calculations and history management took precedence over enhancements like unit conversions (US-005) and exporting history (US-008). Despite this structured approach, there were moments of doubt—was I making the right call? Would I regret postponing certain features? This internal conflict made prioritization an ongoing challenge.

Estimating effort was another area where I struggled. Without a team to discuss complexity levels, I had to rely on personal experience and best guesses to assign story points. Initially, I underestimated the complexity of features like encryption (US-009) and optimization (US-010), assigning them lower story points when, in reality, they required deeper research and testing. Conversely, I overestimated tasks like clearing history (US-003), which turned out to be straightforward. The lack of peer validation made estimation feel more like a guessing game rather than a structured process. I learned that breaking tasks into smaller increments and tracking time spent on each helped refine future estimates.

Since I was both the decision-maker and executor, there were times when internal resistance slowed my progress. Without external accountability, I found myself procrastinating on certain tasks, especially those outside my comfort zone, like UI design and testing. Moving tasks across the GitHub Project Board from "In Progress" to "In Review" required self-discipline—there was no team pushing me to complete them. To combat this, I introduced structured self-check-ins and deadlines, treating each sprint review as if I were presenting to an external stakeholder. While this helped, the lack of external validation still made some tasks feel less urgent than they would in a traditional Agile team setting.

This experience reinforced the importance of self-discipline, structured prioritization, and adaptability. If I were to redo this project, I would integrate external feedback earlier—perhaps seeking input from potential users or mentors—to validate priorities. I also realized the value of time tracking and reflection in improving estimation skills. Moving forward, refining Agile practices through self-imposed deadlines and simulated stakeholder reviews will be key to maintaining motivation and structured progress.

Navigating Agile development as a solo stakeholder has been both rewarding and challenging. While the flexibility allowed me to structure the project on my terms, the absence of external accountability made prioritization, estimation, and execution difficult. By acknowledging these challenges and implementing structured self-discipline techniques, I can refine my Agile approach and ensure continued project.

# Reflection on Using a Kanban Board

## 1. Understanding Kanban as a Project Management Tool  
The Kanban board provided a structured way to visualize tasks and manage workflow efficiently. By breaking down work into stages—Backlog, Ready, In Progress, In Review, Testing, Blocked, and Done —I could track progress clearly and identify bottlenecks.  

## 2. Challenges Faced  
- **Adapting to the Workflow:** Initially, understanding how to properly transition tasks between columns was challenging. Sometimes, tasks were incorrectly placed, leading to confusion.  
- **Task Overload:** Without Work-In-Progress (WIP) limits, multiple tasks were in progress at once, making it difficult to focus. Implementing a limit helped improve efficiency.  
- **Blocked Tasks:** Some tasks remained in "Blocked" for extended periods, which slowed overall progress. Identifying the causes early helped mitigate this issue.  

## 3. Key Takeaways & Learning Experience  
- **Improved Time Management:** The board forced prioritization of tasks, reducing time spent switching between unfinished work.  
- **Better Collaboration:** If used in a team setting, Kanban ensures that everyone knows task statuses and dependencies.  
- **Flexibility:** Unlike rigid project management tools, Kanban allows continuous improvement, adapting workflows as needed.  

## 4. How This Will Be Applied in Future Projects  
Using Kanban has improved my ability to plan and track tasks** effectively. Moving forward, I will:  
- Set realistic WIP limits to maintain focus.  
- Use automation (if available) to transition tasks based on completion criteria.  
- Regularly review the board to remove stale or unnecessary tasks.  

# Reflections for Object state  modeling and activity workflow objective.
## 1. Challenges in Choosing Granularity for States/Actions

One of the main challenges in modeling was deciding the level of granularity. Too much detail makes diagrams cluttered and hard to follow, while too little detail risks missing important transitions or activities. For example, in the Advanced Calculator System, modeling every calculation type as a separate state/action made the diagrams too complex. To balance this, similar actions (like different types of unit conversions) were grouped under broader categories like “Perform Conversion” for simplicity and better readability.

## 2. Aligning Diagrams with Agile User Stories

Another challenge was mapping diagrams accurately to Agile user stories. Agile focuses on delivering small, incremental value through user-centric stories, which sometimes lacked the technical specificity needed for precise diagramming. For example, a user story like “As a user, I want to export my results” required interpreting what backend processes that entails (e.g., generating files, triggering downloads). Ensuring diagrams reflect this functionality without making assumptions required collaboration with stakeholders or clarification of acceptance criteria.

## 3. Comparing State Diagrams vs. Activity Diagrams
Aspect	State Diagrams	Activity Diagrams
Focus	Object behavior over time	Step-by-step process flow
Best for	Lifecycle of a single object	Modeling workflows and system processes
Example Use	Calculator session: Idle → Active → Closed	Export workflow, registration, calculations
Visual Elements	States, transitions, events, guards	Actions, decisions, concurrency, swimlanes
Challenge	Hard to model parallel actions	Less suited for object-level behavior

Summary: State diagrams were ideal for showing how the calculator or user account changes states due to events (e.g., login, session expired), while activity diagrams effectively captured end-to-end workflows such as performing calculations or exporting results.

# Reflections for designing the domain model and class diadram 
Designing the domain model and class diagram for the Advanced Calculator System posed several intellectual and practical challenges. One of the first hurdles was deciding the appropriate level of granularity for domain entities. Initially, there was a temptation to overcomplicate the model by introducing too many minor classes for operations like trigonometric functions, algebraic simplifications, or expression parsing. However, these would clutter the model and hinder readability. After several iterations, I chose to abstract these operations under the Calculator class, with different type values like basic, scientific, and graphing.

Another challenge involved defining clear responsibilities between the User, Calculator, and Calculation classes. To maintain separation of concerns, user authentication was kept strictly within the User class, while all evaluation logic remained in the Calculator class. This decision aligns well with object-oriented principles and ensures flexibility in future extensions such as admin roles or advanced calculators.

Aligning the domain model and class diagram with prior assignments required revisiting the use cases and state/activity diagrams created in Assignment 8. For example, the state transitions for “Perform Calculation” and “Generate Graph” directly informed the methods and class responsibilities in the diagram. The activity diagram's decision points also influenced the inclusion of a centralized ErrorHandler class to manage invalid inputs.

A particularly tricky decision involved inheritance and composition. Initially, the Graph class was modeled as a standalone entity. However, since it shares common attributes like expression and result with Calculation, inheritance was introduced, making Graph a subclass of Calculation. This not only reduced redundancy but also aligned better with real-world object hierarchies, where graphing is an extension of standard calculations.

The process also highlighted the importance of traceability in Agile development. The class diagram directly maps to user stories such as “As a user, I want to calculate an expression” or “As a user, I want to view my history.” Sprint tasks like implementing graph generation and input validation are now clearly associated with the respective methods and classes.

One limitation was that Mermaid.js, while simple and readable, lacks advanced features like visibility modifiers for associations or detailed notes inline. Despite this, it was adequate for representing the key classes, attributes, and methods.

This exercise reinforced the importance of designing software systems with extensibility and maintainability in mind. By creating an abstract yet comprehensive model, future requirements like multi-user collaboration or advanced computation modules can be integrated with minimal structural changes. I also learned that revisiting earlier work—like user stories, functional requirements, and behavior diagrams—ensures that design decisions remain grounded in user and system needs.

In conclusion, this assignment not only deepened my understanding of domain modeling and class diagrams but also illustrated the value of cohesive design in software engineering.

## Assignment 14 Refelctions
# Reflection on Open Source Engagement

Engaging with the open-source community has been both eye-opening and rewarding. At first, I was unsure how others would perceive my Advanced Calculator System. However, seeing the project receive 38 stars and 31 forks reassured me that my effort, structure, and attention to detail were recognized.

Through tagging issues as good-first-issue and feature-request, I made it easier for contributors to get involved. Watching other developers interact with my work, raise suggestions, and show interest made me feel like I was contributing to a broader ecosystem.

One challenge I faced was learning how to structure and write clear issue descriptions for others. It made me think about my work from an outsider’s perspective. Additionally, handling GitHub Actions, templates, and badges taught me the importance of continuous integration in modern development.

This experience made me realize that collaboration isn't always about code contribution. It includes clarity, openness, and appreciation for community feedback. Going forward, I aim to maintain this project actively and welcome more contributors with a stronger support framework, including documentation and contributor guidelines.

Being part of an open-source community transforms a personal project into a shared vision. That is the true power of open collaboration.

