Line-by-line breakdown of what each line in the budget_tracker.py file does.

Lines 1-4: Importing Libraries

# Imports the CSV module to read/write comma-separated value files
import csv

# Imports OS module to interact with the operating system (check if files exist)
import os

# Imports the datetime class to work with dates and times
from datetime import datetime

# Imports defaultdict, a dictionary that provides default values for missing keys
from collections import defaultdict

Lines 6-13: Class Definition and Initialization
#Defines a class (blueprint) called BudgetTracker that contains all our program's functionality
class BudgetTracker:

# Special method that runs automatically when you create a new BudgetTracker object
# "self" refers to the specific instance of the class
def __init__(self):

# Creates a variable to store the filename where budget limits are saved
self.budget_file = "budget_limits.csv"

# Creates a variable to store the filename where expenses are saved
 		self.expenses_file = "expenses.csv"
      
# Creates a variable to store monthly income, starts at 0
self.income = 0

# Creates an empty dictionary to store budget categories and their limits (ex: {"Groceries": 400, "Rent": 1200})
self.budget_limits = {}

# Creates an empty list to store all expense records
self.expenses = []

# Calls the load_data method to read saved data from files when program starts
self.load_data()

Lines 15-27: Loading Budget Data

# Defines a method to load saved data from CSV files
def load_data(self):

# Comment labeling section: describes what this function does (documentation)
"""Load budget limits and expenses from files"""

# Comment: explains the next section of code
# Load budget limits

# Checks if the budget_limits.csv file exists before trying to read it
# Prevents errors on first run when no file exists yet
if os.path.exists(self.budget_file):


# Opens the budget file in read mode ('r')
# "with" ensures the file closes automatically when done
# "as f" creates a variable 'f' to reference the file
with open(self.budget_file, 'r') as f:

# Creates a CSV reader object that can read the file line by line
         			reader = csv.reader(f)

# Skips the first line (header row with "Category, Limit")
# Returns None if file is empty
next(reader, None)  # Skip header

# Loops through each remaining row in the CSV file
for row in reader:


# Checks if row exists and has at least 2 columns (category and limit)
# Prevents errors from empty or incomplete rows
if row and len(row) >= 2:

# Checks if first column says "INCOME"
if row[0] == "INCOME":

# Converts the second column to a decimal number and stores as income
self.income = float(row[1])

# If not INCOME, it’s a regular budget category
else:

# Adds the category (row[0]) and its limit (row[1]) to the dictionary
self.budget_limits[row[0]] = float(row[1])

Lines 29-41: Loading Expense Data
# Comment: now loading the expenses file
# Load expenses

# Checks if expenses.csv exists
if os.path.exists(self.expenses_file):

# Opens expenses file in read mode
with open(self.expenses_file, 'r') as f:
# Creates CSV reader for expenses
reader = csv.reader(f)

# Skips header row ("Date, Category, Amount, Description")
next(reader, None)  # Skip header

# Loops through each expense row
for row in reader:

# Checks row has at least 4 columns (date, category, amount, description)
if row and len(row) >= 4:

# Adds a new dictionary to the expenses list
self.expenses.append({


# Stores the date from first column
'date': row[0],


# Stores the category from second column
'category': row[1],


# Converts amount to decimal number
'amount': float(row[2]),


# Stores the description
'description': row[3]

# Closes the dictionary
})

Lines 43-50: Saving Budget Limits
# Defines method to save budget data to file
def save_budget_limits(self):

# Comment labeling section
"""Save budget limits to file"""

# Opens budget file in write mode ('w') - this overwrites the file 
# newline='' prevents extra blank lines in CSV
with open(self.budget_file, 'w', newline='') as f:


# Creates CSV writer object
writer = csv.writer(f)

# Writes header row to file
writer.writerow(['Category', 'Limit'])

# Writes income as first data row
writer.writerow(['INCOME', self.income])

# Loops through each category-limit pair in the dictionary
for category, limit in self.budget_limits.items():

# Writes each category and it’s limit as a row
writer.writerow([category, limit])

Lines 52-63: Saving Expenses
# Defines method to save expenses to file
def save_expenses(self):

# Comment labeling section
"""Save expenses to file"""

# Opens expenses file in write mode
with open(self.expenses_file, 'w', newline='') as f:

# Creates CSV writer
writer = csv.writer(f)

# Writes header row
writer.writerow(['Date', 'Category', 'Amount', 'Description'])

Loops through each expense dictionary
for expense in self.expenses:

# Starts writing a row
writer.writerow([

# Writes all four pieces of expense data
expense['date'],
expense['category'],
expense['amount'],
expense['description']

# Closes the row
])

Lines 65-854: Budget Setup - Income
# Defines method for initial budget setup
def setup_budget(self):

# Comment labeling section
"""Initial budget setup"""

# Prints header with blank line before (\n = newline)
print("\n=== BUDGET SETUP ===")

# Checks if income hasn’t been set yet
if self.income == 0:

# Starts infinite loop (will break when valid input received)
while True:

# Starts try block to catch errors
try:

# Asks user for income, converts to decimal number
self.income = float(input("Enter your monthly income: $"))

# Checks if income is positive
if self.income > 0:

# Exits the while loop if valid
break

# Error message for negative/zero incom
print("Income must be positive!")

# Catches error if user enters text instead of number
except ValueError:

# Error message for if user enter invalid input
				print("Please enter a valid number!")

# If income already exists
else:

# Shows current income formatted to 2 decimal places
# f-string allows embedded variables in text
print(f"Current monthly income: ${self.income:.2f}")

# Asks if user wants to change income, converts answer to lowercase
change = input("Would you like to change it? (y/n): ").lower()

# If user typed ‘y’
if change == 'y':

# Tries to get new income, keeps old value if invalid
			try:
self.income = float(input("Enter new monthly income: $"))
except ValueError:
print("Invalid input. Keeping current income.")


Lines 87-111: Budget Setup - Categories
# Instructions for category setup
print("\nSet up your budget categories (or press Enter to skip):")

# Suggestions for categories
print("Common categories: Groceries, Rent, Entertainment, Transportation, Utilities, Dining, Shopping, Healthcare")

# Loop for adding multiple categorties
while True:

# Gets category name, and .strip() removes extra spaces
category = input("\nCategory name (or press Enter to finish): ").strip()

# If user pressed Enter without typing anything
if not category:

# Exit the loop
break

# Checks if this category already exists
if category in self.budget_limits:

# Shows existing limit
print(f"Current limit for {category}: ${self.budget_limits[category]:.2f}")

# Asks if they want to update it
change = input("Update? (y/n): ").lower()

# 
if change != 'y':

# Skip to next iteration of loop (ask for another category)
continue

# Start error handling
			try:

# Get budget limit for this category
limit = float(input(f"Budget limit for {category}: $"))

# Check if limit is positive
if limit > 0:

# Store the category and limit in dictionary
self.budget_limits[category] = limit

# Error for zero/negative limits
				else:
					print("Limit must be positive!")

# Error for non-numeric input
except ValueError:
print("Invalid amount!")

# Save all budget data to file
self.save_budget_limits()

# Success message
print("\n Budget setup complete!")

Lines 113-125: Add Expense - Setup
# Method to add a new expense
def add_expense(self):

# Comment labeling section
"""Add a new expense"""

# Header
	print("\n=== ADD EXPENSE ===")

# Checks if budget_limits dictionary is empty
if not self.budget_limits:

# Shows error and exits function early if no categories
print("No budget categories set up yet!")
return

# Comment labeling section
# Show available categories

# Lists all categories for user
print("\nAvailable categories:")

# enumerate() gives both index and value
# Starts counting at 1 instead of 0
# .keys() gets all category names

	for i, category in enumerate(self.budget_limits.keys(), 1):

# Prints numbered list (1. Groceries, 2. Rent, etc.)
print(f"{i}. {category}")

# Adds option to create new category as last number
print(f"{len(self.budget_limits) + 1}. Other (create new category)")


Lines 127-143: Add Expense - Category Selection
# Comment labeling section
# Get category

# Loop until a valid is category selected
 	while True:

# Get user’s choice as integer
try:
choice = int(input("\nSelect category number: "))

# Check if choice is valid existing category
if 1 <= choice <= len(self.budget_limits):

# Convert dict keys to list and get category at index (minus 1 because lists start at 0)
category = list(self.budget_limits.keys())[choice - 1]


# Exit loop with selected category
break

# If they chose “Other” option
elif choice == len(self.budget_limits) + 1:

# Get name for new category
				category = input("Enter new category name: ").strip()

# Get budget limit for new category
limit = float(input(f"Set budget limit for {category}: $"))

# Add new category to dictionary
self.budget_limits[category] = limit

# Save updated budget limits
self.save_budget_limits()

# Exit loop
Break

# Error for out-of-range numbers
else:
print("Invalid choice!")

# Catch both value errors (text input) and index errors
		except (ValueError, IndexError):

# Error message
print("Please enter a valid number!")

Lines 145-158: Add Expense - Amount and Description
# Comment labeling section
# Get amount

# Loop for getting valid amount
while True:

# Get expense amount
try:
amount = float(input("Amount spent: $"))

# Accept if positive, exit loop
if amount > 0:
break

# Error for zero/negative
print("Amount must be positive!")

# Error for non-numeric input
except ValueError:
print("Please enter a valid number!")

# Comment labeling section
# Get description

# Get optional description
description = input("Description (optional): ").strip()

# Use default if user leaves it blank
if not description:
description = "No description"

Lines 160-178: Add Expense - Save and Warnings
# Comment labeling section
# Add expense

# Create a new expense dictionary
expense = {


# Get current date formatted as YYYY-MM-DD
'date': datetime.now().strftime('%Y-%m-%d'),

# Store category, amount, and description
'category': category,
'amount': amount,
‘description': description
}
# Add expense to list
self.expenses.append(expense)

# Save to file
self.save_expenses()

# Confirmation message
print(f"\n✓ Added ${amount:.2f} to {category}")

# Comment labeling section
# Check if over budget

# Calculate total spent in this category 
# List comprehension: sums all expense amounts where category matches
category_total = sum(e['amount'] for e in self.expenses if e['category'] == category)

# Get budget limit for this category
limit = self.budget_limits[category]

# Check if over budget
 	if category_total > limit:

# Warning message with overage amount
print(f"⚠ WARNING: {category} is over budget by ${category_total - limit:.2f}!")

# Check if used more than 80% of budget
elif category_total > limit * 0.8:

# Alert showing percentage used
print(f"⚠ ALERT: {category} is at {(category_total/limit)*100:.1f}% of budget")

Lines 180-194  : View Budget Status - Header
# Method to display budget status
def view_budget_status(self):

# Header
"""Display current budget status"""
print("\n=== BUDGET STATUS ===")

# Check if any categories exist
if not self.budget_limits:
print("No budget categories set up yet!")
return

# Comment labeling section
# Calculate spending per category

# Create defaultdict that defaults to 0.0 for new categories

category_spending = defaultdict(float)

# Loop through all expenses
for expense in self.expenses:

# Add expense amount to that category’s total
category_spending[expense['category']] += expense['amount']

# Sum all spending across categories
total_spent = sum(category_spending.values())

# Sum all budget limits
 total_budget = sum(self.budget_limits.values())

Lines 196-203: View Budget Status - Summary
# Display incom
print(f"\nMonthly Income: ${self.income:.2f}")

# Display total budget
print(f"Total Budget: ${total_budget:.2f}")

# Display total spending
print(f"Total Spent: ${total_spent:.2f}")

# Calculate and show remaining money
print(f"Remaining: ${self.income - total_spent:.2f}\n")


# Print 60 dashes as divider
print("-" * 60)

# Print column headers (<20 means left-align in 20 characters width)
print(f"{'Category':<20} {'Spent':<12} {'Budget':<12} {'Status'}")

# Another divider
print("-" * 60)

Lines 205-224: View Budget Status - Category Details
# Loop through each category and it’s limit
for category, limit in self.budget_limits.items():

# Get amount spent (.get returns 0 if category is not found)
spent = category_spending.get(category, 0)

# Calculate remaining budget
remaining = limit – spent

# Calculate percentage used
		percentage = (spent / limit * 100) if limit > 0 else 0

# Comment labeling section
# Create progress bar

# Set progress bar to 20 characters
bar_length = 20

# Calculate how many characters to fill, min() prevents going over 100%
		filled = int(bar_length * min(spent / limit, 1)) if limit > 0 else 0

# Created bar with filled and empty blocks
bar = '█' * filled + '░' * (bar_length - filled)

# Format status string with bar and percentage
status = f"[{bar}] {percentage:.0f}%"

# Print category row (9.2f means right-align in 9 chars with 2 decimals
print(f"{category:<20} ${spent:>9.2f} ${limit:>9.2f}  {status}")

# Show warning if over budget ('' :20 creates 20 spaces for indentation)
if spent > limit:
print(f"{'':20} ⚠ OVER by ${spent - limit:.2f}")

# Show alert if near limit
 elif percentage > 80:
print(f"{'':20} ⚠ {100 - percentage:.0f}% remaining")

# Bottom divider
print("-" * 60)

Lines 226-239: Monthly Summary - Setup
# Method for detailed summary
def monthly_summary(self):

# Header
	"""Show detailed monthly summary"""
print("\n=== MONTHLY SUMMARY ===")

# Exit if no expenses
if not self.expenses:
print("No expenses recorded yet!")
return

# Comment labeling section
# Group by category

# Creat default dict that defaults to empty list
category_spending = defaultdict(list)

# Loop through expenses
for expense in self.expenses:

# Add each expense to it’s category’s list
category_spending[expense['category']].append(expense)

# Sum all expense amounts
total_spent = sum(e['amount'] for e in self.expenses)

Lines 241-257: Monthly Summary - Overview
# Show totals
print(f"\nTotal Monthly Spending: ${total_spent:.2f}")
print(f"Monthly Income: ${self.income:.2f}")

# Calculate and show savings (income minus spending)
print(f"Net Savings: ${self.income - total_spent:.2f}")

# Count total transactions
print(f"\nNumber of Transactions: {len(self.expenses)}\n")

# Table headers
print("-" * 70)
print(f"{'Category':<20} {'Transactions':<15} {'Total':<12} {'% of Spending'}")
print("-" * 70)

Lines 250-257: Monthly Summary - Category Breakdown
# Loop through categories in alphabetical order
for category in sorted(category_spending.keys()):

# Get list of expenses for this category
expenses = category_spending[category]

# Sum this category’s spending
		category_total = sum(e['amount'] for e in expenses)

# Calculate percentage of total spending
		percentage = (category_total / total_spent * 100) if total_spent > 0 else 0

# Print category stats
		print(f"{category:<20} {len(expenses):<15} ${category_total:>9.2f}  {percentage:>5.1f}%")

# Divider
	print("-" * 70)


Lines 259-264: Monthly Summary - Recent Transactions
# Header for transactions
# Show recent transactions
print("\nRecent Transactions (last 10):")
print("-" * 70)

# Get last 10 expenses (negative index counts from end)
recent = self.expenses[-10:]

# Loop through in reverse order (newest first)
for expense in reversed(recent):

# Print each transaction with formatting
print(f"{expense['date']} | {expense['category']:<15} | ${expense['amount']:>7.2f} | {expense['description']}")

Lines 266-285: Export Data
# Method to export to CSV
def export_data(self):

# Header
"""Export data to CSV"""
print("\n=== EXPORT DATA ===")

# Create filename with timestamp (e.g., budget_export_20260213_143052.csv)
filename = f"budget_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Create new file
with open(filename, 'w', newline='') as f:


# Create CSV writer
writer = csv.writer(f)

# Write header
		writer.writerow(['Date', 'Category', 'Amount', 'Description', 'Budget Limit'])


# Loop through expenses
for expense in self.expenses:

# Get budget limit for this category
			limit = self.budget_limits.get(expense['category'], 0)

# Write expense row with limit included
 writer.writerow([
expense['date'],
expense['category'],
expense['amount'],
expense['description'],
limit
])

# Confirmation
print(f" Data exported to {filename}")

Lines 287-309: Main Program Loop
# Main method that runs the program
def run(self):

# Welcome banner
"""Main program loop"""
print("=" * 50)
print("   PERSONAL BUDGET TRACKER")
print("=" * 50)

# Check if first-time setup is needed
# Check if setup is needed
if not self.budget_limits or self.income == 0:

# Run setup if needed
print("\nFirst time setup required!")
self.setup_budget()

# Infinite loop for menu
while True:

# Display menu options
print("\n" + "=" * 50)
print("MAIN MENU")
print("=" * 50)
print("1. Add Expense")
print("2. View Budget Status")
print("3. Monthly Summary")
print("4. Manage Budget Limits")
print("5. Export Data to CSV")
print("6. Exit")

# Get user’s menu choice
choice = input("\nEnter your choice (1-6): ").strip()

Lines 311-326: Menu Choices
# Call add_expense if user chose 1
if choice == '1':
self.add_expense()

# Call view_budget_status if user chose 2
elif choice == '2':
self.view_budget_status()

# Call monthly_summary if user chose 3
			elif choice == '3':
self.monthly_summary()

# Call setup_budget if user chose 4
elif choice == '4':
self.setup_budget()

# Call export_data if user chose 5
elif choice == '5':
self.export_data()

# Exit message and break out of loop (ends program)
elif choice == '6':
print("\nThank you for using Budget Tracker!")
print("Your data has been saved. Goodbye!")
break

# Error for invalid choises
			else:
print("Invalid choice! Please enter 1-6.")

Lines 328-331: Running the Program
# Comment labeling section
# Run the program

# This checks if the file is being run directly (not imported)
# Prevents code from running if someone imports this as a module
if __name__ == "__main__":
# Creates a new BudgetTracker object (this runs init)
tracker = BudgetTracker()

# Calls the run() method to start the program
tracker.run()


