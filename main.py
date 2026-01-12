# main.py
from models import Expense
from storage import load_expenses, save_expenses

FILENAME = "expenses.json"

print("large expenses : ")
def main():
    expenses = load_expenses(FILENAME)

    while True:
        title = input("Enter expense title (exit to stop): ")
        if title == "exit":
            break

        while True:
            try:
                amount = int(input("Enter amount: "))
                break
            except ValueError:
                print("Invalid amount. Enter a number.")

        category = input("Enter category: ")
        expenses.append(Expense(title, amount, category))

    save_expenses(FILENAME, expenses)

    print("\nLarge expenses:")
    for e in expenses:
        if e.is_large():
            print(f"{e.title} - {e.amount} ({e.category})")


if __name__ == "__main__":
    main()
