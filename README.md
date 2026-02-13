# Python_Personal_Budget_Tracker
How to use:
1.	Save this code as budget_tracker.py
2.	Run it: python budget_tracker.py
3.	On first run, you'll set up your income and budget categories
4.	The program creates two CSV files: 
        budget_limits.csv - stores your budget categories and limits
        expenses.csv - stores all your expenses

Features included:
•	Persistent data storage (survives program restarts)
•	Visual progress bars showing budget usage
•	Warnings when approaching/exceeding limits
•	Monthly summary with spending breakdown
•	Export functionality
•	Easy category management
•	Input validation

How to Use the Program
Menu Options Explained:
1.	Add Expense - Record money you've spent 
        Select from existing categories or create a new one
        Enter the amount
        Add an optional description
2.	View Budget Status - See where you stand 
        Visual progress bars for each category
        Shows how much you've spent vs. your budget
        Warnings appear if you're over budget or near your limit
3.	Monthly Summary - Detailed spending analysis 
        Total spending across all categories
        Number of transactions per category
        Percentage breakdown of your spending
        List of recent transactions
4.	Manage Budget Limits - Update your budget 
        Change your monthly income
        Add new categories
        Modify existing budget limits
5.	Export Data - Save to spreadsheet 
        Creates a timestamped CSV file
        Can open in Excel or Google Sheets for deeper analysis
6.	Exit - Close the program safely
Important Information
Data Storage:
•	Your data is saved in two files in the same folder as the program: 
        budget_limits.csv - Your budget categories and limits
        expenses.csv - All your expense transactions
•	Do not delete these files or you'll lose your data
•	Back them up regularly if you want to keep historical records
Tips for Best Results:
•	Add expenses as they happen (don't wait until end of month)
•	Be consistent with category names
•	Use descriptive labels for expenses so you remember what they were
•	Review your budget status weekly to stay on track
•	Adjust budget limits if you consistently go over in certain categories
Warnings & Alerts:
•	Red warning (⚠) appears when you exceed a category budget
•	Alert shows when you've used 80% or more of a category's budget
•	Use these as signals to cut back spending in that area
Limitations:
•	Currently tracks one month at a time (doesn't automatically reset monthly)
•	All amounts should be in dollars (no multi-currency support)
•	Income and expenses are entered manually (no bank integration)
Troubleshooting:
•	If you get an error, make sure you're entering numbers (not text) for dollar amounts
•	If data seems missing, check that the CSV files are in the same folder as the program
•	To start fresh, delete the CSV files and restart the program
Example Workflow:
1.	Run program → Set income to $3000
2.	Create categories: Groceries ($400), Rent ($1200), Entertainment ($200)
3.	Throughout the month, add expenses as they occur
4.	Check budget status weekly
5.	At month end, view monthly summary
6.	Export data for records, then delete CSV files to start fresh next month
That's everything users need to know to use your program effectively!
