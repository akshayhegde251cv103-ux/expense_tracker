# storage.py
import json
from models import Expense


def load_expenses(filename):
    expenses = []
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            for item in data:
                expenses.append(
                    Expense(
                        item["title"],
                        item["amount"],
                        item["category"]
                    )
                )
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass

    return expenses


def save_expenses(filename, expenses):
    with open(filename, "w") as file:
        json.dump(
            [e.to_dict() for e in expenses],
            file,
            indent=4
        )
