# Simple Expense Tracker
expenses = []

def add_expense(description, amount):
    """Add a new expense"""
    expenses.append({"description": description, "amount": amount})
    print(f"✓ Added: {description} - ${amount}")

def view_expenses():
    """View all expenses"""
    if not expenses:
        print("No expenses yet!")
        return
    
    print("\n--- Your Expenses ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['description']}: ${exp['amount']}")
    print(f"Total: ${sum(e['amount'] for e in expenses)}\n")

def main():
    while True:
        print("\n1. Add expense")
        print("2. View expenses")
        print("3. Exit")
        choice = input("Choose (1-3): ")
        
        if choice == "1":
            desc = input("What did you buy? ")
            amount = float(input("How much? $"))
            add_expense(desc, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
