import json
from models import Expense

def save_expenses(expenses, filename="data/expenses.json"):
    data = [e.to_dict() for e in expenses]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_expenses(filename="data/expenses.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Expense.from_dict(e) for e in data]
    except FileNotFoundError:
        return []