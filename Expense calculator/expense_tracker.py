import csv


class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def to_dict(self):
        return {
            'date': self.date,
            'category': self.category,
            'description': self.description,
            'amount': self.amount
        }


def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    expense = Expense(date, category, description, amount)
    expenses.append(expense)
    save_expenses(expenses)


def view_expenses(expenses):
    for expense in expenses:
        print(f"{expense.date} - {expense.category} - {expense.description} - ${expense.amount:.2f}")


def filter_expenses(expenses, start_date=None, end_date=None, category=None):
    filtered = []
    for expense in expenses:
        if start_date and end_date:
            if start_date <= expense.date <= end_date:
                if category:
                    if expense.category == category:
                        filtered.append(expense)
                else:
                    filtered.append(expense)
        elif category:
            if expense.category == category:
                filtered.append(expense)
        else:
            filtered.append(expense)
    return filtered


def analyze_expenses(expenses):
    total_spent = sum(expense.amount for expense in expenses)
    average_daily_spending = total_spent / len(expenses)
    expenses_by_category = {}
    for expense in expenses:
        if expense.category not in expenses_by_category:
            expenses_by_category[expense.category] = 0
        expenses_by_category[expense.category] += expense.amount

    print(f"Total Spent: ${total_spent:.2f}")
    print(f"Average Daily Spending: ${average_daily_spending:.2f}")
    print("Expenses by Category:")
    for category, amount in expenses_by_category.items():
        print(f"  {category}: ${amount:.2f}")


def export_to_csv(expenses, filename="expenses.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'description', 'amount'])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense.to_dict())

import csv

def load_expenses(filename="data/expenses.csv"):
    expenses = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense = Expense(row['date'], row['category'], row['description'], float(row['amount']))
                expenses.append(expense)
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses, filename="data/expenses.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'description', 'amount'])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense.to_dict())


def main():
    expenses = load_expenses()
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses")
        print("4. Analyze Expenses")
        print("5. Export Data")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            start_date = input("Enter start date (YYYY-MM-DD) or leave blank: ")
            end_date = input("Enter end date (YYYY-MM-DD) or leave blank: ")
            category = input("Enter category or leave blank: ")
            filtered = filter_expenses(expenses, start_date, end_date, category)
            view_expenses(filtered)
        elif choice == '4':
            analyze_expenses(expenses)
        elif choice == '5':
            filename = input("Enter filename to export to (default: expenses.csv): ")
            if not filename:
                filename = "expenses.csv"
            export_to_csv(expenses, filename)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
