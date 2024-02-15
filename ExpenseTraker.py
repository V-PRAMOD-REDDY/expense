import os
import datetime
def get_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
        return [expense.strip() for expense in expenses]
    except FileNotFoundError:
        return []

def save_expense(expense):
    with open("expenses.txt", "a") as file:
        file.write(f"{expense}\n")

def display_expenses():
    expenses = get_expenses()
    if not expenses:
        print("No expenses found.")
    else:
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense}")

def track_expenses():
    while True:
        print("________________________________________")
        print("\nExpense Tracker Menu:")
        print("________________________________________")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            expense_description = input("Enter expense description: ")
            amount = input("Enter amount spent: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            expense = f"{timestamp} - {expense_description} - ${amount}"
            save_expense(expense)
            print("Expense added successfully!")

        elif choice == "2":
            print("\n--- Expenses ---")
            display_expenses()

        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    if not os.path.exists("expenses.txt"):
        with open("expenses.txt", "w"):
            pass
        track_expenses()

