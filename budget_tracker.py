import csv
import os
from datetime import datetime
from collections import defaultdict

class BudgetTracker:
    def __init__(self):
        self.budget_file = "budget_limits.csv"
        self.expenses_file = "expenses.csv"
        self.income = 0
        self.budget_limits = {}
        self.expenses = []
        self.load_data()
    
    def load_data(self):
        """Load budget limits and expenses from files"""
        # Load budget limits
        if os.path.exists(self.budget_file):
            with open(self.budget_file, 'r') as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header
                for row in reader:
                    if row and len(row) >= 2:
                        if row[0] == "INCOME":
                            self.income = float(row[1])
                        else:
                            self.budget_limits[row[0]] = float(row[1])
        
        # Load expenses
        if os.path.exists(self.expenses_file):
            with open(self.expenses_file, 'r') as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header
                for row in reader:
                    if row and len(row) >= 4:
                        self.expenses.append({
                            'date': row[0],
                            'category': row[1],
                            'amount': float(row[2]),
                            'description': row[3]
                        })
    
    def save_budget_limits(self):
        """Save budget limits to file"""
        with open(self.budget_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Category', 'Limit'])
            writer.writerow(['INCOME', self.income])
            for category, limit in self.budget_limits.items():
                writer.writerow([category, limit])
    
    def save_expenses(self):
        """Save expenses to file"""
        with open(self.expenses_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
            for expense in self.expenses:
                writer.writerow([
                    expense['date'],
                    expense['category'],
                    expense['amount'],
                    expense['description']
                ])
    
    def setup_budget(self):
        """Initial budget setup"""
        print("\n=== BUDGET SETUP ===")
        
        if self.income == 0:
            while True:
                try:
                    self.income = float(input("Enter your monthly income: $"))
                    if self.income > 0:
                        break
                    print("Income must be positive!")
                except ValueError:
                    print("Please enter a valid number!")
        else:
            print(f"Current monthly income: ${self.income:.2f}")
            change = input("Would you like to change it? (y/n): ").lower()
            if change == 'y':
                try:
                    self.income = float(input("Enter new monthly income: $"))
                except ValueError:
                    print("Invalid input. Keeping current income.")
        
        print("\nSet up your budget categories (or press Enter to skip):")
        print("Common categories: Groceries, Rent, Entertainment, Transportation, Utilities, Dining, Shopping, Healthcare")
        
        while True:
            category = input("\nCategory name (or press Enter to finish): ").strip()
            if not category:
                break
            
            if category in self.budget_limits:
                print(f"Current limit for {category}: ${self.budget_limits[category]:.2f}")
                change = input("Update? (y/n): ").lower()
                if change != 'y':
                    continue
            
            try:
                limit = float(input(f"Budget limit for {category}: $"))
                if limit > 0:
                    self.budget_limits[category] = limit
                else:
                    print("Limit must be positive!")
            except ValueError:
                print("Invalid amount!")
        
        self.save_budget_limits()
        print("\n Budget setup complete!")
    
    def add_expense(self):
        """Add a new expense"""
        print("\n=== ADD EXPENSE ===")
        
        if not self.budget_limits:
            print("No budget categories set up yet!")
            return
        
        # Show available categories
        print("\nAvailable categories:")
        for i, category in enumerate(self.budget_limits.keys(), 1):
            print(f"{i}. {category}")
        print(f"{len(self.budget_limits) + 1}. Other (create new category)")
        
        # Get category
        while True:
            try:
                choice = int(input("\nSelect category number: "))
                if 1 <= choice <= len(self.budget_limits):
                    category = list(self.budget_limits.keys())[choice - 1]
                    break
                elif choice == len(self.budget_limits) + 1:
                    category = input("Enter new category name: ").strip()
                    limit = float(input(f"Set budget limit for {category}: $"))
                    self.budget_limits[category] = limit
                    self.save_budget_limits()
                    break
                else:
                    print("Invalid choice!")
            except (ValueError, IndexError):
                print("Please enter a valid number!")
        
        # Get amount
        while True:
            try:
                amount = float(input("Amount spent: $"))
                if amount > 0:
                    break
                print("Amount must be positive!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Get description
        description = input("Description (optional): ").strip()
        if not description:
            description = "No description"
        
        # Add expense
        expense = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'category': category,
            'amount': amount,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()
        
        print(f"\n✓ Added ${amount:.2f} to {category}")
        
        # Check if over budget
        category_total = sum(e['amount'] for e in self.expenses if e['category'] == category)
        limit = self.budget_limits[category]
        if category_total > limit:
            print(f"⚠ WARNING: {category} is over budget by ${category_total - limit:.2f}!")
        elif category_total > limit * 0.8:
            print(f"⚠ ALERT: {category} is at {(category_total/limit)*100:.1f}% of budget")
    
    def view_budget_status(self):
        """Display current budget status"""
        print("\n=== BUDGET STATUS ===")
        
        if not self.budget_limits:
            print("No budget categories set up yet!")
            return
        
        # Calculate spending per category
        category_spending = defaultdict(float)
        for expense in self.expenses:
            category_spending[expense['category']] += expense['amount']
        
        total_spent = sum(category_spending.values())
        total_budget = sum(self.budget_limits.values())
        
        print(f"\nMonthly Income: ${self.income:.2f}")
        print(f"Total Budget: ${total_budget:.2f}")
        print(f"Total Spent: ${total_spent:.2f}")
        print(f"Remaining: ${self.income - total_spent:.2f}\n")
        
        print("-" * 60)
        print(f"{'Category':<20} {'Spent':<12} {'Budget':<12} {'Status'}")
        print("-" * 60)
        
        for category, limit in self.budget_limits.items():
            spent = category_spending.get(category, 0)
            remaining = limit - spent
            percentage = (spent / limit * 100) if limit > 0 else 0
            
            # Create progress bar
            bar_length = 20
            filled = int(bar_length * min(spent / limit, 1)) if limit > 0 else 0
            bar = '█' * filled + '░' * (bar_length - filled)
            
            status = f"[{bar}] {percentage:.0f}%"
            
            print(f"{category:<20} ${spent:>9.2f} ${limit:>9.2f}  {status}")
            
            if spent > limit:
                print(f"{'':20} ⚠ OVER by ${spent - limit:.2f}")
            elif percentage > 80:
                print(f"{'':20} ⚠ {100 - percentage:.0f}% remaining")
        
        print("-" * 60)
    
    def monthly_summary(self):
        """Show detailed monthly summary"""
        print("\n=== MONTHLY SUMMARY ===")
        
        if not self.expenses:
            print("No expenses recorded yet!")
            return
        
        # Group by category
        category_spending = defaultdict(list)
        for expense in self.expenses:
            category_spending[expense['category']].append(expense)
        
        total_spent = sum(e['amount'] for e in self.expenses)
        
        print(f"\nTotal Monthly Spending: ${total_spent:.2f}")
        print(f"Monthly Income: ${self.income:.2f}")
        print(f"Net Savings: ${self.income - total_spent:.2f}")
        print(f"\nNumber of Transactions: {len(self.expenses)}\n")
        
        print("-" * 70)
        print(f"{'Category':<20} {'Transactions':<15} {'Total':<12} {'% of Spending'}")
        print("-" * 70)
        
        for category in sorted(category_spending.keys()):
            expenses = category_spending[category]
            category_total = sum(e['amount'] for e in expenses)
            percentage = (category_total / total_spent * 100) if total_spent > 0 else 0
            
            print(f"{category:<20} {len(expenses):<15} ${category_total:>9.2f}  {percentage:>5.1f}%")
        
        print("-" * 70)
        
        # Show recent transactions
        print("\nRecent Transactions (last 10):")
        print("-" * 70)
        recent = self.expenses[-10:]
        for expense in reversed(recent):
            print(f"{expense['date']} | {expense['category']:<15} | ${expense['amount']:>7.2f} | {expense['description']}")
    
    def export_data(self):
        """Export data to CSV"""
        print("\n=== EXPORT DATA ===")
        filename = f"budget_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Category', 'Amount', 'Description', 'Budget Limit'])
            
            for expense in self.expenses:
                limit = self.budget_limits.get(expense['category'], 0)
                writer.writerow([
                    expense['date'],
                    expense['category'],
                    expense['amount'],
                    expense['description'],
                    limit
                ])
        
        print(f" Data exported to {filename}")
    
    def run(self):
        """Main program loop"""
        print("=" * 50)
        print("   PERSONAL BUDGET TRACKER")
        print("=" * 50)
        
        # Check if setup is needed
        if not self.budget_limits or self.income == 0:
            print("\nFirst time setup required!")
            self.setup_budget()
        
        while True:
            print("\n" + "=" * 50)
            print("MAIN MENU")
            print("=" * 50)
            print("1. Add Expense")
            print("2. View Budget Status")
            print("3. Monthly Summary")
            print("4. Manage Budget Limits")
            print("5. Export Data to CSV")
            print("6. Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_budget_status()
            elif choice == '3':
                self.monthly_summary()
            elif choice == '4':
                self.setup_budget()
            elif choice == '5':
                self.export_data()
            elif choice == '6':
                print("\nThank you for using Budget Tracker!")
                print("Your data has been saved. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1-6.")

# Run the program
if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run()