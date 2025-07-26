from datetime import datetime

class Expense:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Expense(data["amount"], data["category"], data["date"])

class Budget:
    def __init__(self):
        self.budgets = {}

    def set_budget(self, category, amount):
        self.budgets[category] = amount

    def get_budget(self, category):
        return self.budgets.get(category, 0)