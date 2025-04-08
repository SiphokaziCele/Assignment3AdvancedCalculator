## Domain Model
| **Entity **      | **Attributes**                                       | **Methods**               
------------------------------------------------------------------------------------------------
| **User**         | `userID`, `name`, `email`,`password`                 | `egister()`, `login()`,`logout()`,
|**Calculator**    | `calculatorID`, `type`,(basic, scientific, graphing) |`calculateExpression


## Domain Model

| **Entity**        | **Attributes**                                                             | **Methods**                                                                 | **Relationships**                                                                                  |
|-------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| **User**          | `userId`, `name`, `email`, `password`                                      | `register()`, `login()`, `logout()`                                         | Can perform Calculations, owns CalculationHistory                                                 |
| **Calculator**    | `calculatorId`, `type` (basic, scientific, graphing)                       | `calculateExpression()`, `validateInput()`, `displayResult()`              | Linked to Calculation, used by User                                                                |
| **Calculation**   | `calculationId`, `expression`, `result`, `timestamp`                       | `perform()`, `saveToHistory()`                                              | Created by Calculator, belongs to User                                                             |
| **Graph**         | `graphId`, `functionExpression`, `graphImage`                              | `generateGraph()`, `renderGraph()`                                          | Subclass of Calculation, visualized by Calculator                                                  |
| **History**       | `historyId`, `userId`, `listOfCalculations`                                | `addEntry()`, `viewHistory()`, `clearHistory()`                             | Associated with User, stores multiple Calculations                                                 |
| **ErrorHandler**  | `errorCode`, `errorMessage`                                                | `catchInputError()`, `logError()`                                           | Handles invalid inputs during Calculation and Graph generation                                     |
