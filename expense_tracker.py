import csv
from datetime import datetime

# File name
FILE_NAME = "expenses.csv"

# Create file with header if not exists
def create_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])
    except FileExistsError:
        pass  # already created


# Add new expense
def add_expense(category, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("✅ Expense added successfully!")


# View all expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# Show total expenses
def total_expenses():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    print(f"💰 Total Expenses: ₹{total}")


# Main menu
def main():
    create_file()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter category (Food/Travel/Other): ")
            amount = input("Enter amount: ")
            add_expense(category, amount)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
