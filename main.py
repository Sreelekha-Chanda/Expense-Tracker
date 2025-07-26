from tracker import ExpenseTracker
from storage import save_expenses, load_expenses

def main():
    tracker = ExpenseTracker()
    tracker.expenses = load_expenses()

    while True:
        print("\n📊 Personal Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Set Monthly Budget")
        print("4. View Budget Status")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amt = float(input("Enter amount: "))
            cat = input("Enter category (e.g., food, transport): ")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            tracker.add_expense(amt, cat, date or None)

        elif choice == "2":
            for e in tracker.expenses:
                print(f"{e.date} | {e.category} | ₹{e.amount}")

        elif choice == "3":
            cat = input("Enter category to set budget: ")
            amt = float(input("Enter monthly budget: "))
            tracker.budget.set_budget(cat, amt)

        elif choice == "4":
            status = tracker.check_budget_status()
            for cat, info in status.items():
                print(f"{cat}: Spent ₹{info['spent']}, Budget ₹{info['budget']}, Remaining ₹{info['remaining']}")

        elif choice == "5":
            save_expenses(tracker.expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()