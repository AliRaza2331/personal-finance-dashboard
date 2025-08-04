# ALI RAZA
# MCS Project 4
# I am the sole author of this project, except where contributions of others
# are noted in README.md.

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database connection
def get_db_connection():
    """
    Establish a connection to the SQLite database.
    Returns conn (sqlite3.Connection), SQLite connection object that can be used
    to perform database operations.
    """
    conn = sqlite3.connect('finance_manager.db')
    conn.row_factory = sqlite3.Row # to make row results accessible by field name
    return conn

# Setup the database table if not exists
def setup_db():
    """
    Creates the necessary database tables if they do not already exist.
    This function sets up a table named 'transactions' with columns for ID, date,
    category, description, and amount.
    """
    with app.app_context():
        db = get_db_connection()
        db.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                date TEXT,
                category TEXT,
                description TEXT,
                amount REAL
            )
        ''')
        db.commit()
        db.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Route to handle the landing page requests. Supports both GET and POST methods.
    1. GET: Renders the homepage with a list of all transactions and the current balance summary.
    2. POST: Processes new transaction data submitted via the form.
    Returns: On GET: HTML page rendered with transaction data and balance summary.
    Returns: On POST: Redirects to the homepage after adding the new transaction to the database.
    """
    db = get_db_connection()
    if request.method == 'POST':
        # Fetch data from form
        category = request.form['category']
        description = request.form['description']
        amount = round(float(request.form['amount']), 2)  # Round amount before storing
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert transaction into database
        db.execute('INSERT INTO transactions (date, category, description, amount) VALUES (?, ?, ?, ?)',
                   (date, category, description, amount))
        db.commit()

        # Redirect to home to refresh the page with new data
        return redirect(url_for('home'))

    # Retrieve transactions from database
    transactions = db.execute('SELECT * FROM transactions').fetchall()
    income, expenses, balance = get_balance_summary(db)
    db.close()
    return render_template('finance_manager.html', transactions=transactions, income=income, expenses=expenses, balance=balance)

def get_balance_summary(db):
    """
    Calculates the total income, expenses, and current balance from the transactions database.
    Args: db (sqlite3.Connection): The database connection object.
    Returns a tuple containing total income, total expenses, and current balance.
    """
    income = round(db.execute('SELECT SUM(amount) FROM transactions WHERE amount > 0').fetchone()[0] or 0, 2)
    expenses = round(db.execute('SELECT SUM(amount) FROM transactions WHERE amount < 0').fetchone()[0] or 0, 2)
    balance = round(income + expenses, 2)
    return income, expenses, balance

if __name__ == '__main__':
    setup_db()  # Ensure the database is setup at launch
    app.run(debug=True)
    

    
