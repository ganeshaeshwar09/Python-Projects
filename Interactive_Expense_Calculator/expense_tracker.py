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
