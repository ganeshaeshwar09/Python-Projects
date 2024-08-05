from flask import Flask, render_template, request, redirect, url_for
from expense_tracker import Expense, load_expenses, save_expenses

app = Flask(__name__)

@app.route('/')
def index():
    expenses = load_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        description = request.form['description']
        amount = float(request.form['amount'])
        expenses = load_expenses()
        expense = Expense(date, category, description, amount)
        expenses.append(expense)
        save_expenses(expenses)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
