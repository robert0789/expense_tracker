# Simple Expense Tracker
Simple expense tracking enable to user write, track, and analyze income and expense from time to time. 
This project aim to help user organize daily spending, keep track on their money flow and as a tool to make it easier to organize financial goals.
The main outputs of this project are organized daily personalized spending and monthly recorded money flow summarization

## User Stories
### Epic 1 : Expense Capture & Logging
- As a user, I want to record income and expense with minimum effort, so i able to create record without any haze
- As a user, I want to record income and expense with date, category, amount, and write a note, so every record is clear and accurate
- As a user, I want to income and expense based added on selected  
### Epic 2: Categorization & Record Management
- As a user, I want to see the history of expense and income record, so that i can review and audit my money flow
- As a user, I want to able modify records of income and expense, so that i can correct any record mistake with ease
- As a user, I want to create a custom category of income and expense, so that each income and expense has meaningful category
### Epic 3: Budgeting & Spend Alert
- As a user, I want to able create monthly budgeting for each expense category, so that i do not overspend
### Epic 4: Data Export, Reporting & Data Insights
-  As a user, I want to view a central dashboard showing my net recorded balance, total income, total expense, net cash flow, remaining budget, and recent transactions.
-  As a user, I want to see a pie chart or bar graph of my expenses broken down by category so that I can visually identify my largest spending habits.
-  As a user, I want to filter my transaction history by date range, category, or payment method so that I can find specific purchases quickly.
-  As a user, I want to export data with custom range of data, so that i can access transaction history without using app

## Core Features
- Simple forms to record expense or income based on date, type (income or expense), category, amount (limited on Rp), note, and optional file attachment and flag for reccuring income/expense
- budgeting window to select category and budget amount for fixed month
- clean table display expense daily record 
- Clean displays showing total income, total spending, and current remaining balance for each month
- Pie graphs, bar charts, and trend lines to break down spending by category or time frame.
- Export record in csv format within range (can be all data)

### Features Priority
| Priority | Features | Criteria |
| -------- | -------- | -------- |
| P0 - Mandatory | CRUD transaction and SQLite  | Data correct, persistent, and have stable ID |
| P0 - Mandatory | Validation and Category | Reject inappropriate input; ensure income and expense category consistency |
| P0 - Mandatory | Financial analysis | Income, expense, net cash flow, and category summarization |
| P0 - Mandatory | Monthly budgeting | Budget per category and usage status is correct |
| P0 - Mandatory | Automated testing | each feature is tested successfully with normal, edge, and error handling |
| P0 - Mandatory | Streamlit Dashboard | each feature is translated successfully into UI  |
| P1 - Target | History filtering and CSV export | user can search record history on date range and export record history in csv|
| P1 - Target | Rule based categorization| keyword that helps category suggestion|


## Non-criteria Features
- attach invoice file as the app run on local machine
- recurring spending tracker and notify upcoming recurring spending (could be day countdown)
- sign in and log in mechanism, as the application is for standalone user
- Any AI injection for automation (like OCR reading, ML spending classification and anomaly detection, predictive budgeting, chatbot, etc)
- Bank or digital wallet data historical integration for seamless automated expense tracker
- generate report for audit-ready reports, flag tax-deductible items, and track subscription renewal cycles.

## Business Rules and Data Model
### Transaction Rules
- Every transaction has unique ID and not changes even when another record got deleted
- date value in transaction form is defaulted as today date
- Every transaction has date, type, category, amount, and optional note
- The nominal value is stored as a positive rupiah integer. The direction of the transaction is determined by the type, not the denomination's sign.
- Updated or deleted transactions should be immediately reflected in all relevant summaries
- SQLite is the sole primary data source. DataFrames can be created temporarily for analysis, but they are not copies of the data source that must be manually synchronized.

### Category Rules
- Categories have two type: income or expense.
- The category used in a transaction must match the transaction type.
- Successfully created custom categories are immediately available for subsequent transactions.
- For categories already used in previous transactions, do not immediately delete the category and its history. In the initial version, you can prohibit the deletion of categories that are still in use.

### Budget Rules
- Budgets are only available monthly for the first version.
- Expenses for a specific category and month are calculated based on expense transactions dated within that month.
- The remaining budget is calculated using the formula: Remaining Budget = Budget - Expense Total
- The remaining budget may be negative to indicate that the budget limit has been exceeded.
- The budget must be greater than zero for the usage percentage to be calculated.

### Reporting rules
- reporting shows the total income, total expense, net recorded balance, and remaining budget on time monthly horizon

## Acceptance Criteria
### Expense Capture & Logging
- Given a user is on the "Add Transaction" screen, when they input an amount , select a category and type, pick a date, write note, attach file and flag recurring spending if needed, and submit, then the record is **saved into SQLite** and immediately appears in the transaction history list.
- Forms able to prevent user from submit appropriate data, i.e., leaving the type and category select blank and amount is not number or negative number.

### Categorization & Record Management
- Given a user enter main dashboard, the record of expense tracker is display cleanly, and highlight today spending 
- Given a user creates a custom category (e.g., "Pets"), when user click the add category button, then the new category **saved into SQLite** and available in the dropdown selection for all future expense entries
- Given a user on a records of income and expense, when user can click the update button. Update will lead to the form with placeholder existing data, with same validation data as expense entry, user click the submit update data,  **updated data saved back to SQLite and system will recalculate the data summarize** and user are back to main dashboard and updated data is shown or record history with pop up update data successfully. 
- Given a user on a records of income and expense, when user click the delete button, the confirmation window will show up to confirm the delete process and **data will deleted on SQLite and system recalculate the data summarization**,  Pop up window will notify the record has successfully deleted and deleted data won't show in the record history, as the system shows updated data summarization

### Budgeting & Spend Alert
- Given a user sets a monthly budget limit, example of Rp1.000.000 for the "Groceries" category, when their total expenses in that category reach Rp500.000, Rp750.000, Rp900.000 and Rp1.000.000 or cross it, then the status on the dashboard appear on different color tone (dark green as expense exceed 50% , yellow as expense exceed 75%, orange as expense exceed 90%, red as expense exceed 100%). 

### Data Export, Reporting & Data Insights
- Given a user click the export button, user are navigate time horizon selection to date range picker (from date picker - to date picker) and a checker for all data, the system will execute download the csv of historical expense record (with all its column) and user able to access the csv offline. If the transaction is empty, system will inform to user in the pop up window
- Given a user navigates to the analytics or reports tab, when transactions exist for the selected month, then a pie chart or bar graph accurately displays spending breakdown per category
- Given the expense transactions for the selected month, when the dashboard displays a category graph, the value of each category is equal to the aggregated expense transactions for that month, and the total sum of the graph is equal to the total expenses for the same period.

## Technical Approach
### Development Environment
- IDE: Visual Studio Code
- Programming Language: Python 3.12
- Database: SQLite
- Data Analysis: pandas
- User Interface: Streamlit
- Testing Framework: pytest
- Version Control: Git and GitHub

Python dependencies will be managed using a virtual environment and recorded in requirements.txt. The application should be runnable locally without requiring a cloud service, external database server, or user authentication.

### Application Architecture
The application will use a simple layered architecture to separate user interaction, business logic, and data persistence.

text [ Black Space / User
  |
  v
Streamlit UI (app.py)
  |
  v
Service Layer (service.py)
  |
  v
Repository Layer (repository.py)
  |
  v
SQLite Database ]

**Responsibilities**
- UI Layer (app.py): Handles user input, forms, transaction history, dashboard components, charts, filters, and messages displayed to users.
- Service Layer (service.py): Implements business rules, input validation, transaction operations, financial calculations, budget monitoring, and category-related logic.
- Repository Layer (repository.py): Handles SQLite queries and database operations, including creating, retrieving, updating, and deleting records.
- Database: Permanently stores transaction, category, and budget records.
Additional modules, such as models.py or categorizer.py, may be introduced when they provide a clear separation of responsibilities. The architecture should remain simple and avoid unnecessary abstractions.

### Data Storage and Management
SQLite will serve as the single source of truth for persistent application data.
The initial database will contain the following entities:
- Transactions: Transaction ID, date, type, category ID, amount, and optional note.
- Categories: Category ID, category name, and transaction type.
- Budgets: Budget ID, category ID, period, and budget amount.
Transaction IDs will be stable identifiers used for update and delete operations. Amounts will be stored as positive integer values in Indonesian rupiah (IDR), while the transaction type determines whether the amount represents income or expense.
Pandas DataFrames may be used temporarily for data analysis and visualization, but they will not act as a separate source of truth.

### Business Logic
The business logic will be implemented independently of the UI so calculations and validation can be tested without running the Streamlit application.
Core operations include:
- Creating, retrieving, updating, and deleting transactions.
- Validating transaction dates, amounts, types, and categories.
- Calculating total income, total expenses, and net cash flow.
- Aggregating expenses by category and month.
- Calculating budget utilization and remaining budget.
- Categorizing transaction descriptions using predefined rules.
- Filtering transactions and preparing data for CSV export.
Functions should return predictable data types and raise meaningful exceptions when an operation cannot be completed. UI components will handle those exceptions and present appropriate messages to users.

### Testing Strategy
Automated tests will be implemented using pytest. Tests will focus on business logic, database operations, input validation, and the consistency of financial calculations.

The testing strategy includes:
- Normal cases: Valid inputs and expected successful operations.
- Edge cases: Empty datasets, boundary values, missing optional notes, and transactions at date or budget boundaries.
- Error cases: Invalid amounts, invalid categories, malformed dates, nonexistent transaction IDs, and database operation failures.

Database tests will use a temporary or isolated SQLite database to avoid modifying real application data. Tests must import and execute the actual production modules rather than redefining copies of the application classes.

### Data Visualization and Export
Streamlit will provide the dashboard and transaction management interface. Pandas will support data aggregation where appropriate, while charts will display expense breakdowns and trends.

CSV export will support user-selected date ranges, including the option to export all transactions. Exported data must match the selected filters and use a consistent column structure.

### Scope and Design Constraints
The initial version will prioritize correctness, maintainability, and usability for local applications.
The following are outside the initial scope:
- Authentication and multi-user support.
- Bank or digital wallet integration.
- AI-based categorization, OCR, prediction, or anomaly detection.
- Automatic scheduling of recurring transactions.
- Invoice attachment and cloud deployment.

Additional features may be considered once core acceptance criteria are met. Any scope changes should be evaluated against existing project deadlines and milestones.

## Project Milestone
- Day 1–3 (16-18 oct) Scope locked, final acceptance criteria, repository and project environment ready
- Day4 –10 (19-25 oct) Data model, SQLite, operations repository, and responsibility boundaries
- Day 11–20 (26 oct - 4 Nov) CRUD, categories, validation, stable IDs, and automated testing
- Day 21–30 (5-14 Nov) Financial calculations, category analysis, monthly analysis, and budgeting
- 31–38 (15-22 Noc) Rule-based categorization and rule-based categorization testing
- 39–48 (23 Nov–2 Des) Streamlit dashboard with summary, history, basic filters, and graphs
- 49–54 (3–8 Des) CSV export, integration measurement, and edge case fixes
- 55–60 (9–14 Des) Documentation, demos, clean checks, and bug buffer

## Definition of Done
- CRUD transactions work, and data persists after the application is restarted.
- Balance, net cash flow, category analysis, and budget consistency with transaction data.
- Input errors are rejected with clear behavior.
- Tests import actual production implementations, not sponsored synthetic classes, into the test files.
- Database operations and business logic have normal tests and relevant edge/error cases.
- Dashboards display both normal and empty data states without crashes.
- CSV exports produce data that matches user filters.
- The README explains how to install, run the application, and run tests.
- creator can explain the main design rationale, application limitations, and intentionally left out sections.


