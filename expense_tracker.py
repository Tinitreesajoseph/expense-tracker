from flask import Flask, render_template, request, redirect, url_for
import datetime
import json
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP

app = Flask(__name__)

class ExpenseTracker:
    def __init__(self):
        self.data_file = Path("expenses.json")
        self.transactions = self.load_data()
        self.categories = [
            "Housing", "Transportation", "Food", "Utilities", 
            "Healthcare", "Entertainment", "Shopping", "Income", "Other"
        ]

    def load_data(self):
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                # Convert stored amounts to Decimal
                for transaction in data["transactions"]:
                    transaction["amount"] = str(transaction["amount"])  # Convert float to string for Decimal
                return data
        return {"transactions": [], "monthly_budgets": {}}

    def save_data(self):
        # Convert Decimal objects to float for JSON serialization
        data_to_save = {
            "transactions": [
                {**t, "amount": float(t["amount"])} 
                for t in self.transactions["transactions"]
            ],
            "monthly_budgets": self.transactions["monthly_budgets"]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data_to_save, f, indent=2)

    def add_transaction(self, amount, category, description, date=None, transaction_type="expense"):
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Convert amount to Decimal and round to 2 decimal places
        decimal_amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        transaction = {
            "date": date,
            "amount": str(decimal_amount),  # Store as string to preserve precision
            "category": category,
            "description": description,
            "type": transaction_type
        }
        
        self.transactions["transactions"].append(transaction)
        self.save_data()

    def get_monthly_report(self, year, month):
        target_date = f"{year}-{month:02d}"
        monthly_transactions = [
            t for t in self.transactions["transactions"]
            if t["date"].startswith(target_date)
        ]

        # Use Decimal for calculations
        total_income = sum(
            Decimal(t["amount"]) 
            for t in monthly_transactions 
            if t["type"] == "income"
        ).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        total_expenses = sum(
            Decimal(t["amount"]) 
            for t in monthly_transactions 
            if t["type"] == "expense"
        ).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        return {
            "total_income": str(total_income),
            "total_expenses": str(total_expenses)
        }

tracker = ExpenseTracker()

@app.route('/')
def index():
    current_date = datetime.datetime.now()
    monthly_report = tracker.get_monthly_report(current_date.year, current_date.month)
    recent_transactions = tracker.transactions["transactions"][-5:] if tracker.transactions["transactions"] else []
    
    # Convert amounts to Decimal for template
    for transaction in recent_transactions:
        transaction["amount"] = Decimal(transaction["amount"]).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP
        )
    
    return render_template(
        'index.html',
        report={
            "total_income": Decimal(monthly_report["total_income"]),
            "total_expenses": Decimal(monthly_report["total_expenses"])
        },
        categories=tracker.categories,
        recent_transactions=recent_transactions
    )

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    tracker.add_transaction(
        amount=request.form['amount'],
        category=request.form['category'],
        description=request.form['description'],
        date=request.form['date'],
        transaction_type=request.form['type']
    )
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)