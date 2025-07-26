from models import Expense, Budget

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = Budget()

    def add_expense(self, amount, category, date=None):
        self.expenses.append(Expense(amount, category, date))

    def view_expenses(self, filter_by=None, value=None):
        if not filter_by:
            return self.expenses
        return [e for e in self.expenses if getattr(e, filter_by) == value]

    def get_total_by_category(self):
        summary = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount
        return summary

    def check_budget_status(self):
        total_by_category = self.get_total_by_category()
        status = {}
        for category, budget_amount in self.budget.budgets.items():
            spent = total_by_category.get(category, 0)
            status[category] = {
                "spent": spent,
                "budget": budget_amount,
                "remaining": budget_amount - spent
            }
        return status