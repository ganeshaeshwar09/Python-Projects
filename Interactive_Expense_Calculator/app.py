from flask import Flask, render_template, request, redirect, url_for
from expense_tracker import Expense, load_expenses, save_expenses

app = Flask(__name__)


@app.route('/')
def index():
    expenses = load_expenses()
    return render_template('index.html', expenses=expenses)


@app.route('/submit', methods=['POST'])
def submit():
    date = request.form['date']
    category = request.form['category']
    description = request.form['description']
    amount = float(request.form['amount'])
    expenses = load_expenses()
    expense = Expense(date, category, description, amount)
    expenses.append(expense)
    save_expenses(expenses)
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    expenses = load_expenses()
    expense = expenses[id]

    if request.method == 'POST':
        expenses[id].date = request.form['date']
        expenses[id].category = request.form['category']
        expenses[id].description = request.form['description']
        expenses[id].amount = float(request.form['amount'])
        save_expenses(expenses)
        return redirect(url_for('index'))

    return render_template('edit.html', id=id, expense=expense)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    expenses = load_expenses()
    expenses.pop(id)
    save_expenses(expenses)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
