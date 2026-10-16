# Simple Expense Tracker
simple expense tracking enable to user write, track, and analyze income and expense from time to time

## User Stories
### Epic 1 : Expense Capture & Logging
- As a user, I want to record income and expense with minimum effort, so i able to create record without any haze
- As a user, I want to record income and expense with date, category, amount, note and able to attach invoice, so every record is clear and accurate
- As a user, I want to mark an expense as recurring (e.g., monthly subscriptions or rent) so that the app automatically logs it each cycle without my intervention.
### Epic 2: Categorization & Record Management
- As a user, I want to see the history of expense and income record, so that i can review and audit my money flow
- As a user, I want to able modify records of income and expense, so that i can correct any record mistake with ease
- As a user, I want to create a custom category of income and expense, so that each income and expense has meaningful category
### Epic 3: Budgeting & Spend Alert
- As a user, I want to able create time horizon budgeting (e.g., weekly or monthly) for each expense category, so that i do not overspend
- As a user, I want receive spending alert based on the interval budget remaining (50%, 75%, 95%, 100%), so that i always be notified on my budget limit
### Epic 4: Data Export, Reporting & Data Insights
-  As a user, I want to view a central dashboard showing my total balance, total monthly expenses, remaining budget, and recent transactions.
-  As a user, I want to see a pie chart or bar graph of my expenses broken down by category so that I can visually identify my largest spending habits.
-  As a user, I want to filter my transaction history by date range, category, or payment method so that I can find specific purchases quickly.
-  As a user, I want to export data with custom range of data, so that i can access transaction history without using app

## Core Features
- Simple forms to record expense or income based on date, type (income or expense), category, amount (limited on Rp), note, and optional file attachment and flag for reccuring income/expense
- budgeting window to select category and budget amount for fixed week / month
- notification in the main dashboard when budget limit is within percentage (50%, 75%, 95%, 100%)
- notification for upcoming recurring expense with see details (category, amount, and total amount for all recurring spend) 
- clean table display expense record grouped by nested time horizon (day, week, and month)
- Clean displays showing total income, total spending, and current remaining balance for week or month
- Pie graphs, bar charts, and trend lines to break down spending by category or time frame.
- Export record in csv format within range (can be all data)

## Non-criteria Features
- sign in and log in mechanism, as the application is for standalone user
- Any AI injection for automation (like OCR reading, ML spending classification and anomaly detection, predictive budgeting, chatbot, etc)
- Bank or digital wallet data historical integration for seamless automated expense tracker
- generate report for audit-ready reports, flag tax-deductible items, and track subscription renewal cycles.

## Acceptance Criteria
### Expense Capture & Logging
- Given a user is on the "Add Transaction" screen, when they input an amount , select a category and type, pick a date, write note, attach file and flag recurring spending if needed, and submit, then the record is saved and immediately appears in the transaction history list.
- Forms able to prevent user from submit appropriate data, i.e., leaving the type and category select blank and amount is not number or negative number.

### Categorization & Record Management
- Given a user enter main dashboard, the record of expense tracker is display cleanly in nested time horizon, and highlight today spending 
- Given a user creates a custom category (e.g., "Pets"), when saved, it becomes available in the dropdown selection for all future expense entries
- Given a user on a records of income and expense, user can click the update button. Update will lead to the form with placeholder existing data, with same validation data, user click the submit update data, and user are back to main dashboard with pop up update data successfully
- Given a user on a records of income and expense, user can click the delete button. Pop up window will notify the record has successfully deleted and deleted data won't show in the record history

### Budgeting & Spend Alert
- Given a user sets a monthly budget limit, example of Rp1.000.000 for the "Groceries" category, when their total expenses in that category reach Rp500.000, Rp750.000, Rp900.000 and Rp1.000.000 or cross it, then the system triggers an warning/banner message on the dashboard on different color tone (green, yellow, orange, red)

### Data Export, Reporting & Data Insights
- Given a user click the export button, user are navigate time horizon selection to date range picker (from date picker - to date picker) and a checker for all data, the system will execute download the csv and user able to access the csv offline
- Given a user navigates to the analytics or reports tab, when transactions exist for the selected month, then a pie chart or bar graph accurately displays spending breakdown per category



