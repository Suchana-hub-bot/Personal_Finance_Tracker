import datetime
import calendar

class FinanceTracker:
    def __init__(self):
        self.income = {}  # Store income as {category: [amounts]}
        self.expenses = {}  # Store expenses as {category: [amounts]}
        self.budget = {}  # Store budget as {category: amount}

    def add_income(self):
        category = input("Enter income category (e.g., salary, investments,etc): ")
        while True:
            try:
                amount = float(input("Enter income amount: "))
                if amount < 0:
                    print("Income amount cannot be negative. Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the income amount.")
        if category in self.income:
            self.income[category].append(amount)
        else:
            self.income[category] = [amount]
        print(f"Income of {amount} added to {category} category.")

    def add_expense(self):
        category = input("Enter expense category (e.g., food, rent, utilities): ")
        while True:
            try:
                amount = float(input("Enter expense amount: "))
                if amount < 0:
                    print("Expense amount cannot be negative. Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the expense amount.")
        if category in self.expenses:
            self.expenses[category].append(amount)
        else:
            self.expenses[category] = [amount]
        print(f"Expense of {amount} added to {category} category.")

    def set_budget(self):
        category = input("Enter budget category (e.g., food, rent, utilities): ")
        while True:
            try:
                amount = float(input("Enter budget amount: "))
                if amount < 0:
                    print("Budget amount cannot be negative. Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the budget amount.")
        self.budget[category] = amount
        print(f"Budget of {amount} set for {category} category.")

    def generate_financial_report(self):
        print("\n--- Financial Report ---")
        total_income = 0
        for category, amounts in self.income.items():
            category_total = sum(amounts)
            total_income += category_total
            print(f"Income from {category}: {category_total:.2f}")
        print(f"Total Income: {total_income:.2f}")

        total_expenses = 0
        for category, amounts in self.expenses.items():
            category_total = sum(amounts)
            total_expenses += category_total
            print(f"Expense for {category}: {category_total:.2f}")
        print(f"Total Expenses: {total_expenses:.2f}")

        print("\n--- Budget Summary ---")
        for category, amount in self.budget.items():
            actual_expense = sum(self.expenses.get(category, [0]))  #handles the case where a category exists in budget but not in expenses
            variance = amount - actual_expense
            print(f"Budget for {category}: {amount:.2f}, Actual Expense: {actual_expense:.2f}, Variance: {variance:.2f}")
            overall_balance = total_income - total_expenses
        print(f"\nOverall Balance: {overall_balance:.2f}")
        if overall_balance >= 0:
            print("You are within your budget.")
        else:
            print("You are over your budget.")
    
    def view_summary(self):
        print("\n--- Income Summary ---")
        if not self.income:
            print("No income recorded.")
        else:
            for category, amounts in self.income.items():
                print(f"{category}: {amounts}")

        print("\n--- Expenses Summary ---")
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for category, amounts in self.expenses.items():
                print(f"{category}: {amounts}")

        print("\n--- Budget Summary ---")
        if not self.budget:
            print("No budget set.")
        else:
            for category, amount in self.budget.items():
                print(f"{category}: {amount}")

    def display_menu(self):
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. Generate Financial Report")
        print("5. View Summary") #added view summary
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_income()
            elif choice == '2':
                self.add_expense()
            elif choice == '3':
                self.set_budget()
            elif choice == '4':
                self.generate_financial_report()
            elif choice == '5': #added option to view summary
                self.view_summary()
            elif choice == '6':
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = FinanceTracker()
    tracker.run()